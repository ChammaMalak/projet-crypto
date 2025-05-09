# twofish.py

"""
Implémentation du chiffrement Twofish (Finaliste AES).
"""

from Crypto.Cipher import Twofish
from Crypto.Random import get_random_bytes
from binascii import hexlify, unhexlify

def encrypt(key, plaintext):
    """
    Chiffre un texte en clair avec Twofish en utilisant la clé donnée.
    """
    cipher = Twofish.new(key, Twofish.MODE_ECB)
    
    # S'assurer que le texte est un multiple de 16 octets (tail taille du bloc Twofish)
    while len(plaintext) % 16 != 0:
        plaintext += ' '
    
    # Chiffrement
    ciphertext = cipher.encrypt(plaintext.encode('utf-8'))
    return hexlify(ciphertext).decode('utf-8')

def decrypt(key, ciphertext):
    """
    Déchiffre un texte chiffré avec Twofish en utilisant la clé donnée.
    """
    cipher = Twofish.new(key, Twofish.MODE_ECB)
    
    # Convertir en octets
    ciphertext = unhexlify(ciphertext)
    
    # Déchiffrement
    decrypted_text = cipher.decrypt(ciphertext).decode('utf-8').rstrip()
    return decrypted_text

# Exemple d'utilisation
if __name__ == "__main__":
    key = get_random_bytes(32)  # Twofish peut utiliser une clé de 128, 192 ou 256 bits
    plaintext = "Hello, this is Twofish encryption!"
    
    print(f"Texte en clair : {plaintext}")
    
    ciphertext = encrypt(key, plaintext)
    print(f"Texte chiffré : {ciphertext}")
    
    decrypted_text = decrypt(key, ciphertext)
    print(f"Texte déchiffré : {decrypted_text}")
