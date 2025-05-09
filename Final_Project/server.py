#  server.py (bidirectional caesar communication)
import socket
import threading

def caesar_encrypt(text, key):
    result = ''
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def caesar_decrypt(text, key):
    return caesar_encrypt(text, -key)

def receive_messages(conn, key):
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                print("[Client disconnected]")
                break
            encrypted_msg = data.decode()
            decrypted_msg = caesar_decrypt(encrypted_msg, key)
            print(f"\n[Encrypted]: {encrypted_msg}")
            print(f"[Decrypted]: {decrypted_msg}")
        except:
            break

HOST = '0.0.0.0'
PORT = 12345
KEY = 3

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"[+] Server listening on port {PORT}...")

conn, addr = server_socket.accept()
print(f"[+] Connected by {addr}")

# Start receiving in a separate thread
recv_thread = threading.Thread(target=receive_messages, args=(conn, KEY))
recv_thread.daemon = True
recv_thread.start()

# Main thread sends messages
while True:
    try:
        reply = input("You: ")
        encrypted = caesar_encrypt(reply, KEY)
        conn.send(encrypted.encode())
    except:
        break

conn.close()
server_socket.close()
