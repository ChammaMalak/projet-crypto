"""
Chiffrement de Vigenère
-------------------------
Chaque lettre du message est chiffrée par une lettre de la clé répétée.
Les caractères non alphabétiques sont conservés (espaces, ponctuation).
"""

from ast import main


def validate_key(key):
    """Vérifie que la clé contient uniquement des lettres."""
    if not key.isalpha():
        raise ValueError("La clé doit contenir uniquement des lettres.")

def repeat_key(key, length):
    """Répète ou tronque la clé pour qu'elle ait la même taille que le message (lettres seulement)."""
    key = key.upper()
    return (key * (length // len(key) + 1))[:length]

def encrypt(plaintext, key):
    """
    Chiffre le texte clair avec l'algorithme de Vigenère.
    Garde les caractères non alphabétiques (espaces, ponctuation).
    """
    validate_key(key)
    plaintext = plaintext.upper()
    key = repeat_key(key, sum(c.isalpha() for c in plaintext))

    ciphertext = ''
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            p = ord(char) - ord('A')
            k = ord(key[key_index]) - ord('A')
            encrypted_char = chr((p + k) % 26 + ord('A'))
            ciphertext += encrypted_char
            key_index += 1
        else:
            ciphertext += char  # Conserver les caractères non alphabétiques

    return ciphertext

def decrypt(ciphertext, key):
    """
    Déchiffre un texte chiffré avec l'algorithme de Vigenère.
    Garde les caractères non alphabétiques (espaces, ponctuation).
    """
    validate_key(key)
    ciphertext = ciphertext.upper()
    key = repeat_key(key, sum(c.isalpha() for c in ciphertext))

    plaintext = ''
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            c = ord(char) - ord('A')
            k = ord(key[key_index]) - ord('A')
            decrypted_char = chr((c - k + 26) % 26 + ord('A'))
            plaintext += decrypted_char
            key_index += 1
        else:
            plaintext += char  # Conserver les caractères non alphabétiques

    return plaintext


# Exemple d'utilisation
if __name__ == "__main__":
    message = "ATTACK AT DAWN!"
    key = "LEMON"

    print("Message original :", message)
    print("Clé :", key)

    encrypted = encrypt(message, key)
    print("Texte chiffré :", encrypted)

    decrypted = decrypt(encrypted, key)
    print("Texte déchiffré :", decrypted)
if __name__ == "__main__":
    main()
