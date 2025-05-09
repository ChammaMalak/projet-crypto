# affine.py

"""
Chiffrement Affine
-------------------
Utilise une fonction affine pour chiffrer et déchiffrer un message.
Formule : E(x) = (ax + b) mod 26, D(x) = a^-1 * (x - b) mod 26
"""

import string

def gcd(a, b):
    """Calcul du plus grand commun diviseur (PGCD) de a et b."""
    while b:
        a, b = b, a % b
    return a


def mod_inverse(a, m):
    """Calcule l'inverse modulaire de a sous modulo m."""
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None  # Si l'inverse modulaire n'existe pas


def affine_encrypt(plaintext, a, b):
    """Chiffre le texte clair avec la clé affine (a, b)."""
    # Vérification que 'a' et 26 sont premiers entre eux (pgcd(a, 26) == 1)
    if gcd(a, 26) != 1:
        raise ValueError("a et 26 doivent être premiers entre eux (pgcd(a, 26) = 1)")

    plaintext = plaintext.upper().replace(" ", "")
    ciphertext = ""

    for char in plaintext:
        if char.isalpha():
            x = ord(char) - ord('A')  # Convertir la lettre en une valeur numérique (0-25)
            encrypted_char = (a * x + b) % 26
            ciphertext += chr(encrypted_char + ord('A'))
        else:
            ciphertext += char  # Gérer les caractères non alphabétiques (espaces, etc.)

    return ciphertext


def affine_decrypt(ciphertext, a, b):
    """Déchiffre le texte chiffré avec la clé affine (a, b)."""
    if gcd(a, 26) != 1:
        raise ValueError("a et 26 doivent être premiers entre eux (pgcd(a, 26) = 1)")

    # Trouver l'inverse modulaire de 'a' sous modulo 26
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        raise ValueError("L'inverse de 'a' n'existe pas. Assurez-vous que 'a' est valide.")

    decrypted_text = ""

    for char in ciphertext:
        if char.isalpha():
            y = ord(char) - ord('A')  # Convertir la lettre en une valeur numérique (0-25)
            decrypted_char = (a_inv * (y - b)) % 26
            decrypted_text += chr(decrypted_char + ord('A'))
        else:
            decrypted_text += char  # Gérer les caractères non alphabétiques

    return decrypted_text


# Exemple d'utilisation
if __name__ == "__main__":
    message = "HELLO WORLD"
    a = 5  # Choisir un 'a' tel que gcd(a, 26) = 1
    b = 8  # Choisir un 'b'

    print("Message original :", message)
    print("Clé a :", a, "Clé b :", b)

    encrypted = affine_encrypt(message, a, b)
    print("Texte chiffré :", encrypted)

    decrypted = affine_decrypt(encrypted, a, b)
    print("Texte déchiffré :", decrypted)
