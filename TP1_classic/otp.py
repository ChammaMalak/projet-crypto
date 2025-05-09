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

# Fonctions à utiliser depuis main.py
def otp_encrypt(message, preserve_spaces=False):
    key = generate_random_key(len(message.replace(" ", "")) if not preserve_spaces else len(message))
    ciphertext = encrypt(message, key, preserve_spaces)
    return ciphertext, key

def otp_decrypt(ciphertext, key, preserve_spaces=False):
    return decrypt(ciphertext, key, preserve_spaces)
