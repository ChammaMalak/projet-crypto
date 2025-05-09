from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# AES-128 key (must be 16 bytes)
key = b'16byteslongkey!!'

def aes_encrypt(plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_text = pad(plaintext.encode(), AES.block_size)
    ciphertext = cipher.encrypt(padded_text)
    return ciphertext

def aes_decrypt(ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted.decode()

def main():
    print("\n--- AES (ECB mode) ---")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()

    if choice == 'E':
        plaintext = input("Enter the plaintext: ")
        encrypted = aes_encrypt(plaintext)
        print("Encrypted (bytes):", encrypted)
        print("Encrypted (hex):", encrypted.hex())
    elif choice == 'D':
        hex_input = input("Enter the ciphertext (hex): ")
        try:
            ciphertext = bytes.fromhex(hex_input)
            decrypted = aes_decrypt(ciphertext)
            print("Decrypted text:", decrypted)
        except Exception as e:
            print("Decryption failed:", e)
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()
