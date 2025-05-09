from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# DES key (must be exactly 8 bytes)
key = b'8bytekey'

def des_encrypt(plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plaintext.encode(), DES.block_size)
    ciphertext = cipher.encrypt(padded_text)
    return ciphertext

def des_decrypt(ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = unpad(cipher.decrypt(ciphertext), DES.block_size)
    return decrypted_text.decode()

def main():
    print("\n--- DES (ECB mode) ---")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()

    if choice == 'E':
        plaintext = input("Enter the plaintext: ")
        encrypted = des_encrypt(plaintext)
        print("Encrypted (bytes):", encrypted)
        print("Encrypted (hex):", encrypted.hex())
    elif choice == 'D':
        hex_input = input("Enter the ciphertext (hex): ")
        try:
            ciphertext = bytes.fromhex(hex_input)
            decrypted = des_decrypt(ciphertext)
            print("Decrypted text:", decrypted)
        except Exception as e:
            print("Decryption failed:", e)
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()
