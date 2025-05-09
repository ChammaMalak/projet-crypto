"""
Examen de Kasiski pour un texte chiffré.
Cette méthode est utilisée pour casser des chiffres comme Vigenère.
"""

import re

def kasiski_examination(ciphertext):
    """
    Effectue l'examen de Kasiski sur un texte chiffré.
    Trouve les répétitions de séquences de caractères et calcule les distances entre elles.
    """
    # Trouver les séquences répétées dans le texte chiffré
    sequences = {}
    for i in range(len(ciphertext) - 2):  # Examiner des séquences de 3 caractères
        sequence = ciphertext[i:i+3]
        if sequence in sequences:
            sequences[sequence].append(i)
        else:
            sequences[sequence] = [i]

    # Calculer les distances entre les répétitions de séquences
    distances = []
    for sequence, positions in sequences.items():
        if len(positions) > 1:  # On ne prend en compte que les séquences répétées
            for i in range(1, len(positions)):
                distance = positions[i] - positions[i-1]
                distances.append(distance)

    return distances

def main():
    print("\n--- Kasiski Examination ---")
    ciphertext = input("Enter the ciphertext to perform Kasiski examination: ")
    
    # Effectuer l'examen de Kasiski
    distances = kasiski_examination(ciphertext)
    print(f"Distances between repetitions: {distances}")

# Exemple d'utilisation (sera ignoré si le module est importé)
if __name__ == "__main__":
    main()
