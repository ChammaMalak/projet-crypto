# substitution.py

"""
Chiffrement par Substitution
-----------------------------
Chaque lettre du texte clair est remplacée par une lettre correspondante dans un alphabet mélangé.
"""

import string
import random

def generate_random_alphabet():
    """Génère un alphabet mélangé aléatoirement."""
    alphabet = list(string.ascii_uppercase)
    random.shuffle(alphabet)
    return ''.join(alphabet)


def substitution_encrypt(plaintext, key):
    """Chiffre le texte clair en utilisant la clé de substitution."""
    plaintext = plaintext.upper().replace(" ", "")  # Conversion en majuscules et suppression des espaces
    ciphertext = ""
    
    # Créer un dictionnaire de substitution basé sur la clé
    substitution_dict = {string.ascii_uppercase[i]: key[i] for i in range(26)}

    # Substitution de chaque caractère du texte clair
    for char in plaintext:
        if char.isalpha():  # Ne traiter que les lettres
            ciphertext += substitution_dict[char]
        else:
            ciphertext += char  # Gérer les caractères non alphabétiques (espaces, etc.)

    return ciphertext


def substitution_decrypt(ciphertext, key):
    """Déchiffre le texte chiffré en utilisant la clé de substitution."""
    ciphertext = ciphertext.upper().replace(" ", "")  # Conversion en majuscules et suppression des espaces
    plaintext = ""

    # Créer un dictionnaire de déchiffrement basé sur la clé
    reverse_substitution_dict = {key[i]: string.ascii_uppercase[i] for i in range(26)}

    # Substitution inverse de chaque caractère du texte chiffré
    for char in ciphertext:
        if char.isalpha():  # Ne traiter que les lettres
            plaintext += reverse_substitution_dict[char]
        else:
            plaintext += char  # Gérer les caractères non alphabétiques

    return plaintext


# Exemple d'utilisation
if __name__ == "__main__":
    message = "HELLO WORLD"
    key = generate_random_alphabet()  # Générer une clé aléatoire

    print("Message original :", message)
    print("Clé de substitution :", key)

    encrypted = substitution_encrypt(message, key)
    print("Texte chiffré :", encrypted)

    decrypted = substitution_decrypt(encrypted, key)
    print("Texte déchiffré :", decrypted)
