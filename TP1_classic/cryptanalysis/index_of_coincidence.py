"""
Calcul de l'indice de coïncidence pour un texte chiffré.
Cette méthode est utilisée pour détecter des chiffres mono-alphabétiques comme César et Substitution.
"""

import string
from collections import Counter

def index_of_coincidence(ciphertext):
    """
    Calcule l'indice de coïncidence pour un texte chiffré.
    L'indice de coïncidence est une mesure de la probabilité que deux lettres prises au hasard dans un texte soient égales.
    """
    # Filtrer les caractères non alphabétiques et convertir en majuscules
    ciphertext = ''.join([char for char in ciphertext.upper() if char in string.ascii_uppercase])
    
    # Compter les occurrences des lettres dans le texte chiffré
    letter_counts = Counter(ciphertext)
    
    # Calculer l'indice de coïncidence
    total_letters = sum(letter_counts.values())
    ic = sum(count * (count - 1) for count in letter_counts.values()) / (total_letters * (total_letters - 1))
    
    return ic

def main():
    print("\n--- Index of Coincidence ---")
    ciphertext = input("Enter the ciphertext to calculate the Index of Coincidence: ")
    
    # Calculer l'indice de coïncidence
    ic = index_of_coincidence(ciphertext)
    print(f"Index of Coincidence: {ic:.4f}")

# Exemple d'utilisation (sera ignoré si le module est importé)
if __name__ == "__main__":
    main()
