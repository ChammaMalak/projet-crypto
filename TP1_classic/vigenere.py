# vigenere.py

"""
Chiffrement de Vigenère
-------------------------
Chaque lettre du message est chiffrée par une lettre de la clé répétée.
Ex : clé = LEMON, message = ATTACK => chiffrement lettre par lettre.
"""

def repeat_key(key, length):
    """Répète ou tronque la clé pour qu'elle ait la même taille que le message."""
    key = key.upper()
    return (key * (length // len(key) + 1))[:length]

def encrypt(plaintext, key):
    """
    Chiffre le texte clair avec l'algorithme de Vigenère.
    """
    plaintext = ''.join([char for char in plaintext.upper() if char.isalpha()])
    key = repeat_key(key, len(plaintext))

    ciphertext = ''
    for p, k in zip(plaintext, key):
        # (position lettre + position clé) % 26
        encrypted_char = chr((ord(p) - ord('A') + ord(k) - ord('A')) % 26 + ord('A'))
        ciphertext += encrypted_char

    return ciphertext

def decrypt(ciphertext, key):
    """
    Déchiffre un texte chiffré avec l'algorithme de Vigenère.
    """
    ciphertext = ''.join([char for char in ciphertext.upper() if char.isalpha()])
    key = repeat_key(key, len(ciphertext))

    plaintext = ''
    for c, k in zip(ciphertext, key):
        # (position lettre - position clé + 26) % 26
        decrypted_char = chr((ord(c) - ord('A') - (ord(k) - ord('A')) + 26) % 26 + ord('A'))
        plaintext += decrypted_char

    return plaintext


# Exemple d'utilisation
if __name__ == "__main__":
    message = "ATTACKATDAWN"
    key = "LEMON"

    encrypted = encrypt(message, key)
    print("Texte chiffré :", encrypted)  # Exemple : LXFOPVEFRNHR

    decrypted = decrypt(encrypted, key)
    print("Texte déchiffré :", decrypted)  # ATTACKATDAWN
