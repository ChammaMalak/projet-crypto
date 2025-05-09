# playfair.py

"""
Chiffrement de Playfair
------------------------
Algorithme basé sur une matrice 5x5 générée à partir d'une clé.
Chaque paire de lettres est chiffrée selon sa position dans la matrice.
"""

import string

def prepare_key(key):
    """Crée une grille 5x5 à partir de la clé (lettre J fusionnée avec I)."""
    key = key.upper().replace('J', 'I')
    seen = set()
    matrix = []

    for char in key + string.ascii_uppercase:
        if char not in seen and char.isalpha():
            seen.add(char)
            matrix.append(char)
    return [matrix[i:i+5] for i in range(0, 25, 5)]


def format_plaintext(text):
    """Formate le texte clair : enlève les espaces, double lettres, et sépare par paires."""
    text = text.upper().replace('J', 'I')
    cleaned = ''
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'X'

        if a == b:
            cleaned += a + 'X'
            i += 1
        else:
            cleaned += a + b
            i += 2
    if len(cleaned) % 2 != 0:
        cleaned += 'X'
    return [cleaned[i:i+2] for i in range(0, len(cleaned), 2)]


def find_position(matrix, char):
    """Retourne la position (ligne, colonne) du caractère dans la matrice."""
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None, None


def encrypt_pair(matrix, a, b):
    """Chiffre une paire de lettres selon les règles de Playfair."""
    row_a, col_a = find_position(matrix, a)
    row_b, col_b = find_position(matrix, b)

    if row_a == row_b:
        # Même ligne
        return matrix[row_a][(col_a + 1) % 5] + matrix[row_b][(col_b + 1) % 5]
    elif col_a == col_b:
        # Même colonne
        return matrix[(row_a + 1) % 5][col_a] + matrix[(row_b + 1) % 5][col_b]
    else:
        # Rectangle
        return matrix[row_a][col_b] + matrix[row_b][col_a]


def decrypt_pair(matrix, a, b):
    """Déchiffre une paire de lettres selon les règles de Playfair."""
    row_a, col_a = find_position(matrix, a)
    row_b, col_b = find_position(matrix, b)

    if row_a == row_b:
        return matrix[row_a][(col_a - 1) % 5] + matrix[row_b][(col_b - 1) % 5]
    elif col_a == col_b:
        return matrix[(row_a - 1) % 5][col_a] + matrix[(row_b - 1) % 5][col_b]
    else:
        return matrix[row_a][col_b] + matrix[row_b][col_a]


def encrypt(plaintext, key):
    """Fonction principale de chiffrement Playfair."""
    matrix = prepare_key(key)
    pairs = format_plaintext(plaintext)
    return ''.join([encrypt_pair(matrix, a, b) for a, b in pairs])


def decrypt(ciphertext, key):
    """Fonction principale de déchiffrement Playfair."""
    matrix = prepare_key(key)
    pairs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
    return ''.join([decrypt_pair(matrix, a, b) for a, b in pairs])


# Exemple
if __name__ == "__main__":
    key = "MONARCHY"
    message = "HELLO WORLD"

    encrypted = encrypt(message, key)
    print("Texte chiffré :", encrypted)

    decrypted = decrypt(encrypted, key)
    print("Texte déchiffré :", decrypted)
