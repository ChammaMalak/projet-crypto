#  client.py (bidirectional caesar communication)
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

def receive_messages(sock, key):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                print("[Server disconnected]")
                break
            decrypted = caesar_decrypt(data.decode(), key)
            print(f"\nServer: {decrypted}")
        except:
            break

HOST = '192.168.100.5'  # Replace with your PC's IP
PORT = 12345
KEY = 3

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print("[+] Connected to server. Type your messages below:")

# Start a thread to receive messages from server
recv_thread = threading.Thread(target=receive_messages, args=(client_socket, KEY))
recv_thread.daemon = True
recv_thread.start()

while True:
    msg = input("You: ")
    encrypted = caesar_encrypt(msg, KEY)
    client_socket.send(encrypted.encode())
