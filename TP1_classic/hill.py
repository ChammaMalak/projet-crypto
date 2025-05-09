from ast import main
import numpy as np

def mod_inverse_matrix(matrix, modulus):
    """
    Calcule l'inverse d'une matrice modulo 26 (nécessaire pour le déchiffrement).
    """
    det = int(round(np.linalg.det(matrix)))
    det_inv = pow(det, -1, modulus)  # Calculate modular inverse of determinant
    if det_inv == 0:
        raise ValueError("La matrice clé n'est pas inversible modulo 26.")
    matrix_mod_inv = (
        det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    )
    return matrix_mod_inv


def text_to_numbers(text):
    """Convertit un texte en liste de nombres (A=0, B=1, ..., Z=25)."""
    return [ord(char) - ord('A') for char in text.upper() if char.isalpha()]


def numbers_to_text(numbers):
    """Convertit une liste de nombres en texte (0=A, ..., 25=Z)."""
    return ''.join([chr(num % 26 + ord('A')) for num in numbers])


def pad_text(text, block_size, pad_char='X'):
    """Ajoute des caractères de padding à la fin si le texte n'est pas un multiple de la taille du bloc."""
    text = ''.join([char for char in text.upper() if char.isalpha()])
    while len(text) % block_size != 0:
        text += pad_char
    return text


def encrypt(plaintext, key_matrix):
    """
    Chiffre le texte avec l'algorithme de Hill.
    """
    block_size = key_matrix.shape[0]
    plaintext = pad_text(plaintext, block_size)
    numbers = text_to_numbers(plaintext)
    ciphertext = []

    for i in range(0, len(numbers), block_size):
        block = np.array(numbers[i:i+block_size])
        encrypted_block = np.dot(key_matrix, block) % 26
        ciphertext.extend(encrypted_block)

    return numbers_to_text(ciphertext)


def decrypt(ciphertext, key_matrix):
    """
    Déchiffre le texte chiffré avec l'algorithme de Hill.
    """
    block_size = key_matrix.shape[0]
    numbers = text_to_numbers(ciphertext)
    plaintext = []

    try:
        inverse_key = mod_inverse_matrix(key_matrix, 26)
    except ValueError as e:
        return str(e)

    for i in range(0, len(numbers), block_size):
        block = np.array(numbers[i:i+block_size])
        decrypted_block = np.dot(inverse_key, block) % 26
        plaintext.extend(decrypted_block)

    return numbers_to_text(plaintext)


# Exemple d'utilisation
if __name__ == "__main__":
    # Clé 2x2 : doit être inversible modulo 26
    key = np.array([[3, 3], [2, 5]])

    message = "HELLO"
    encrypted = encrypt(message, key)
    print("Texte chiffré :", encrypted)

    decrypted = decrypt(encrypted, key)
    print("Texte déchiffré :", decrypted)

if __name__ == "__main__":
    main()
