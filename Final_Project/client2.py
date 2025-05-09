# client2.py (bidirectional AES communication)
import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

KEY = b'ThisIsSecretKey!'  # 16 bytes

def encrypt_aes(plaintext):
    iv = get_random_bytes(16)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return iv, ciphertext

def decrypt_aes(ciphertext, iv):
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext.decode()

HOST = '192.168.100.7'  # Replace with your PC's IP
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    message = input("[You]: ")
    iv, ciphertext = encrypt_aes(message)
    client_socket.sendall(iv + ciphertext)

    # Receive server response
    response_iv = client_socket.recv(16)
    response_ciphertext = client_socket.recv(1024)
    reply = decrypt_aes(response_ciphertext, response_iv)
    print(f"[Server]: {reply}")

client_socket.close()
