# server2.py (bidirectional AES communication)
import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

KEY = b'ThisIsSecretKey!'  # 16 bytes

def decrypt_aes(ciphertext, iv):
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext.decode()

def encrypt_aes(plaintext):
    iv = get_random_bytes(16)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return iv, ciphertext

HOST = '0.0.0.0'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"[+] Server listening on port {PORT}...")

conn, addr = server_socket.accept()
print(f"[+] Connected by {addr}")

while True:
    try:
        iv = conn.recv(16)
        if not iv:
            break
        ciphertext = conn.recv(1024)
        if not ciphertext:
            break

        print(f"[IV]: {iv.hex()}")
        print(f"[Ciphertext]: {ciphertext.hex()}")

        decrypted = decrypt_aes(ciphertext, iv)
        print(f"[Decrypted]: {decrypted}")

        # Send encrypted reply
        reply = input("[Server → Client]: ")
        reply_iv, reply_ciphertext = encrypt_aes(reply)
        conn.sendall(reply_iv + reply_ciphertext)

    except Exception as e:
        print(f"[Error] {e}")
        break

conn.close()
