# index_of_coincidence.py

"""
Calcul de l'Indice de Coïncidence (IC) pour un texte chiffré.
L'IC permet d'identifier la probabilité que le texte soit mono-alphabétique.
"""

import string
from collections import Counter

def index_of_coincidence(ciphertext):
    """
    Calcule l'Indice de Coïncidence (IC) pour un texte chiffré.
    """
    # Filtrer les caractères non alphabétiques et convertir en majuscules
    ciphertext = ''.join([char for char in ciphertext.upper() if char in string.ascii_uppercase])
    
    # Compter les occurrences des lettres
    letter_counts = Counter(ciphertext)
    
    # Calcul de l'IC : somme des (n * (n-1)) / (N * (N-1)) où n est la fréquence d'une lettre et N le nombre total de lettres
    N = sum(letter_counts.values())
    ic = sum(count * (count - 1) for count in letter_counts.values()) / (N * (N - 1)) if N > 1 else 0
    
    return ic

# Exemple d'utilisation
if __name__ == "__main__":
    ciphertext = "WKH QXFN IHPXQ"
    ic = index_of_coincidence(ciphertext)
    print(f"Indice de coïncidence : {ic}")
