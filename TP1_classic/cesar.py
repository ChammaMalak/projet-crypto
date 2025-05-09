# cesar.py

"""
Chiffrement de César
--------------------
Algorithme de chiffrement monoalphabétique basé sur un décalage fixe des lettres.
"""

def encrypt(plaintext, shift):
    """
    Chiffre le texte en décalant chaque lettre de 'shift' positions vers la droite.
    
    :param plaintext: Le texte à chiffrer (str)
    :param shift: Le décalage (int)
    :return: Le texte chiffré (str)
    """
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            # Décalage circulaire dans l'alphabet
            shifted = (ord(char) - base + shift) % 26 + base
            ciphertext += chr(shifted)
        else:
            ciphertext += char  # On garde les caractères non-alphabétiques (espaces, ponctuation...)
    return ciphertext


def decrypt(ciphertext, shift):
    """
    Déchiffre le texte en inversant le décalage.
    
    :param ciphertext: Le texte chiffré (str)
    :param shift: Le décalage utilisé lors du chiffrement (int)
    :return: Le texte déchiffré (str)
    """
    return encrypt(ciphertext, -shift)  # Déchiffrer = chiffrer avec décalage négatif


# Exemple d'utilisation
if __name__ == "__main__":
    message = "Bonjour le mone !"
    decalage = 3

    chiffre = encrypt(message, decalage)
    print("Texte chiffré :", chiffre)

    dechiffre = decrypt(chiffre, decalage)
    print("Texte déchiffré :", dechiffre)
