import socket
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from Crypto.Random.random import getrandbits

# Fonction pour recevoir exactement 'length' octets
def recv_all(sock, length):
    data = b''
    while len(data) < length:
        packet = sock.recv(length - len(data))
        if not packet:
            raise ConnectionError("Connexion interrompue pendant la réception")
        data += packet
    return data

# Paramètres Diffie-Hellman
p = 23
g = 5

HOST = '192.168.100.5'  # IP du serveur
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"[+] Server listening on port {PORT}")

conn, addr = server_socket.accept()
print(f"[+] Connected by {addr}")

try:
    # Clé privée/publique DH serveur
    private_key = getrandbits(256)
    public_key = pow(g, private_key, p)

    # Envoi de la clé publique DH au client
    print("[Server] Envoi de la clé DH...")
    conn.send(str(public_key).encode())

    # Réception de la clé publique DH client
    client_pub = int(conn.recv(1024).decode())

    # Calcul de la clé partagée
    shared_key = pow(client_pub, private_key, p)
    aes_key = shared_key.to_bytes(16, 'big')[:16]
    print(f"[Server] Clé AES dérivée: {aes_key.hex()}")

    # Générer clés RSA pour le serveur (signature)
    rsa_key = RSA.generate(2048)
    private_rsa = rsa_key
    public_rsa = rsa_key.publickey()

    # Envoi de la clé publique RSA au client
    pubkey_bytes = public_rsa.export_key()
    conn.send(len(pubkey_bytes).to_bytes(4, 'big'))
    conn.send(pubkey_bytes)

    while True:
        # Recevoir IV (16 octets)
        iv = recv_all(conn, 16)

        # Recevoir longueur du ciphertext (4 octets), puis ciphertext
        ct_length_bytes = recv_all(conn, 4)
        ct_length = int.from_bytes(ct_length_bytes, 'big')
        ciphertext = recv_all(conn, ct_length)

        # Recevoir signature (256 octets)
        signature = recv_all(conn, 256)

        # Recevoir longueur clé publique client (4 octets), puis clé
        key_length_bytes = recv_all(conn, 4)
        key_length = int.from_bytes(key_length_bytes, 'big')
        client_pubkey_data = recv_all(conn, key_length)
        client_pubkey = RSA.import_key(client_pubkey_data)

        # Déchiffrement AES
        cipher = AES.new(aes_key, AES.MODE_CBC, iv)
        decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size).decode()

        # Vérification de la signature
        h = SHA256.new(ciphertext)
        try:
            pkcs1_15.new(client_pubkey).verify(h, signature)
            print(f"[Client]: {decrypted} (Signature OK)")
        except (ValueError, TypeError):
            print(f"[Client]: {decrypted} (Signature invalide)")

        # 🔸 Demander au serveur d’écrire une réponse manuellement
        response_msg = input("Server (your message): ")

        # Chiffrement AES de la réponse
        response_cipher = AES.new(aes_key, AES.MODE_CBC)
        response_iv = response_cipher.iv
        response_ciphertext = response_cipher.encrypt(pad(response_msg.encode(), AES.block_size))

        # Signature de la réponse
        h_resp = SHA256.new(response_ciphertext)
        response_signature = pkcs1_15.new(private_rsa).sign(h_resp)

        # Envoi réponse au client
        conn.sendall(response_iv)
        conn.sendall(len(response_ciphertext).to_bytes(4, 'big'))
        conn.sendall(response_ciphertext)
        conn.sendall(response_signature)

        # Envoi clé publique RSA serveur (avec taille)
        conn.sendall(len(pubkey_bytes).to_bytes(4, 'big'))
        conn.sendall(pubkey_bytes)

except Exception as e:
    print(f"[Error] {e}")

finally:
    conn.close()
    server_socket.close()
    print("[Server] Connexion fermée")
    print("[Server] Socket fermé")
    print("[Server] Fin du programme")
