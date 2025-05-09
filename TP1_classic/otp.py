# otp.py

"""
One-Time Pad (OTP)
------------------
Chiffrement par addition modulaire avec une clé aléatoire de même taille que le message.
Sécurité parfaite si la clé respecte les conditions.
"""

import random
import string

def generate_random_key(length):
    """Génère une clé aléatoire de lettres majuscules de longueur égale au message."""
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))


def encrypt(plaintext, key):
    """Chiffre le message avec la clé par addition mod 26 (lettres A-Z)."""
    plaintext = plaintext.upper().replace(" ", "")
    ciphertext = ""

    for p, k in zip(plaintext, key):
        p_val = ord(p) - ord('A')
        k_val = ord(k) - ord('A')
        c_val = (p_val + k_val) % 26
        ciphertext += chr(c_val + ord('A'))

    return ciphertext


def decrypt(ciphertext, key):
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
    message = "CRYPTOGRAPHY"
    key = generate_random_key(len(message))

    print("Message original :", message)
    print("Clé aléatoire     :", key)

    encrypted = encrypt(message, key)
    print("Texte chiffré     :", encrypted)

    decrypted = decrypt(encrypted, key)
    print("Texte déchiffré   :", decrypted)
