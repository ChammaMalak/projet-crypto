def ksa(key): 
    """Key Scheduling Algorithm (KSA)""" 
    key_length = len(key) 
    S = list(range(256)) 
    j = 0 
 
    for i in range(256): 
        j = (j + S[i] + key[i % key_length]) % 256 
        S[i], S[j] = S[j], S[i] 
 
    return S 
 
def prga(S): 
    """Pseudo-Random Generation Algorithm (PRGA)""" 
    i = j = 0 
    while True: 
        i = (i + 1) % 256 
        j = (j + S[i]) % 256 
        S[i], S[j] = S[j], S[i] 
        yield S[(S[i] + S[j]) % 256] 
 
def rc4(key, text): 
    """RC4 encryption/decryption""" 
    key = [ord(c) for c in key] 
    S = ksa(key) 
    keystream = prga(S) 
    return bytes([ord(c) ^ next(keystream) for c in text]) 

def main():
    print("\n--- RC4 Stream Cipher ---")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()
    key = input("Enter the key: ")

    if choice == 'E':
        plaintext = input("Enter the plaintext: ")
        encrypted = rc4(key, plaintext)
        print("Encrypted (bytes):", encrypted)
        print("Encrypted (hex):", encrypted.hex())
    elif choice == 'D':
        hex_input = input("Enter the ciphertext (hex): ")
        try:
            ciphertext = bytes.fromhex(hex_input)
            decrypted = rc4(key, ciphertext.decode('latin1'))
            print("Decrypted text:", decrypted.decode('latin1'))
        except Exception as e:
            print("Decryption failed:", e)
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()
