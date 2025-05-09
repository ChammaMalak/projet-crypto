from ast import main
import random
import string

def generate_random_key(length):
    """Génère une clé aléatoire de lettres majuscules de longueur égale au message."""
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))


def encrypt(plaintext, key, preserve_spaces=False):
    """Chiffre le message avec la clé par addition mod 26 (lettres A-Z)."""
    plaintext = plaintext.upper().replace(" ", "") if not preserve_spaces else plaintext.upper()
    ciphertext = ""

    for p, k in zip(plaintext, key):
        p_val = ord(p) - ord('A')
        k_val = ord(k) - ord('A')
        c_val = (p_val + k_val) % 26
        ciphertext += chr(c_val + ord('A'))

    return ciphertext


def decrypt(ciphertext, key, preserve_spaces=False):
    """Déchiffre le message chiffré avec la clé (soustraction mod 26)."""
    plaintext = ""

    for c, k in zip(ciphertext, key):
        c_val = ord(c) - ord('A')
        k_val = ord(k) - ord('A')
        p_val = (c_val - k_val) % 26
        plaintext += chr(p_val + ord('A'))

    return plaintext


# Exemple d'utilisation
if __name__ == "__main__":
    message = input("Enter the message to encrypt (no spaces allowed for OTP): ")
    preserve_spaces = input("Would you like to preserve spaces (yes/no)? ").lower() == 'yes'
    
    if len(message) == 0:
        print("Message cannot be empty!")
    else:
        key = generate_random_key(len(message))
        print(f"Message original: {message}")
        print(f"Random key: {key}")

        encrypted = encrypt(message, key, preserve_spaces)
        print(f"Encrypted message: {encrypted}")

        decrypted = decrypt(encrypted, key, preserve_spaces)
        print(f"Decrypted message: {decrypted}")
if __name__ == "__main__":
    main()
