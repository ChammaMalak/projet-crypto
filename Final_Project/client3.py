import socket
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random.random import getrandbits

# Fonction pour tout recevoir
def recv_all(sock, length):
    data = b''
    while len(data) < length:
        packet = sock.recv(length - len(data))
        if not packet:
            raise ConnectionError("Connexion interrompue")
        data += packet
    return data

# DH
p = 23
g = 5
private_key = getrandbits(256)
public_key = pow(g, private_key, p)

HOST = '192.168.100.5'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
print("[Client] Connecté au serveur")

# DH
print("[Client] Réception de la clé DH du serveur...")
server_pub = int(client_socket.recv(1024).decode())
print("[Client] Envoi de la clé DH...")
client_socket.send(str(public_key).encode())

shared_key = pow(server_pub, private_key, p)
aes_key = shared_key.to_bytes(16, 'big')[:16]
print(f"[Client] Clé AES dérivée: {aes_key.hex()}")

# ---------------------- RÉCEPTION DE LA CLÉ PUBLIQUE RSA SERVEUR ----------------------
key_length_bytes = recv_all(client_socket, 4)
key_length = int.from_bytes(key_length_bytes, 'big')
rsa_data = recv_all(client_socket, key_length)
server_public_rsa = RSA.import_key(rsa_data)

# Générer clés RSA client
rsa_key = RSA.generate(2048)
private_rsa = rsa_key
public_rsa = rsa_key.publickey()

while True:
    try:
        msg = input("You: ")
        cipher = AES.new(aes_key, AES.MODE_CBC)
        iv = cipher.iv
        ciphertext = cipher.encrypt(pad(msg.encode(), AES.block_size))

        # Signature
        h = SHA256.new(ciphertext)
        signature = pkcs1_15.new(private_rsa).sign(h)

        # Envoi message
        client_socket.sendall(iv)
        client_socket.sendall(len(ciphertext).to_bytes(4, 'big'))
        client_socket.sendall(ciphertext)
        client_socket.sendall(signature)

        # Envoi clé publique client avec taille
        pubkey_bytes = public_rsa.export_key()
        client_socket.sendall(len(pubkey_bytes).to_bytes(4, 'big'))
        client_socket.sendall(pubkey_bytes)

        # ---------------------- RÉCEPTION RÉPONSE ----------------------
        print("[Client] En attente de la réponse...")

        response_iv = recv_all(client_socket, 16)

        response_length_bytes = recv_all(client_socket, 4)
        response_length = int.from_bytes(response_length_bytes, 'big')
        response_ciphertext = recv_all(client_socket, response_length)

        response_signature = recv_all(client_socket, 256)

        # Clé publique serveur renvoyée
        key_length = int.from_bytes(recv_all(client_socket, 4), 'big')
        server_pubkey_bytes = recv_all(client_socket, key_length)
        server_pubkey = RSA.import_key(server_pubkey_bytes)

        # Déchiffrer
        response_cipher = AES.new(aes_key, AES.MODE_CBC, response_iv)
        decrypted = unpad(response_cipher.decrypt(response_ciphertext), AES.block_size).decode()

        h = SHA256.new(response_ciphertext)
        try:
            pkcs1_15.new(server_pubkey).verify(h, response_signature)
            print(f"[Server]: {decrypted} (Signature OK)")
        except:
            print(f"[Server]: {decrypted} (Signature invalide)")

    except Exception as e:
        print(f"[Error] {e}")
        break

client_socket.close()
print("[Client] Connexion fermée")