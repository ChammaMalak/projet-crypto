# kasiski.py

"""
Examen de Kasiski pour casser un chiffre de Vigenère en trouvant la longueur de la clé.
"""

import re
from collections import defaultdict

def kasiski_examination(ciphertext):
    """
    Applique l'examen de Kasiski pour trouver la longueur de la clé du chiffre de Vigenère.
    """
    # Filtrer les caractères non alphabétiques et convertir en majuscules
    ciphertext = ''.join([char for char in ciphertext.upper() if char.isalpha()])
    
    # Dictionnaire pour stocker les positions des répétitions de séquences
    sequences = defaultdict(list)
    
    # Trouver les répétitions de séquences de 3 lettres
    for i in range(len(ciphertext) - 2):
        seq = ciphertext[i:i+3]
        sequences[seq].append(i)
    
    # Calculer les distances entre les répétitions
    distances = []
    for seq, positions in sequences.items():
        if len(positions) > 1:
            for i in range(1, len(positions)):
                distances.append(positions[i] - positions[i - 1])
    
    return distances

# Exemple d'utilisation
if __name__ == "__main__":
    ciphertext = "AAXXYAAWYYZABXAXY"
    distances = kasiski_examination(ciphertext)
    print(f"Distances entre les répétitions : {distances}")
