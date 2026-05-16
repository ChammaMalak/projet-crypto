import string
from collections import Counter

def get_factors(n):
    """Trouve les diviseurs d'un nombre pour suggérer la taille de la clé."""
    factors = []
    # On teste les longueurs de clé probables entre 2 et 12
    for i in range(2, 13):
        if n % i == 0:
            factors.append(i)
    return factors

def kasiski_examination(ciphertext):
    """
    Effectue l'examen de Kasiski sur un texte chiffré.
    Trouve les répétitions de séquences de 3 caractères et calcule les distances.
    """
    # Nettoyage du texte : garder uniquement les lettres A-Z
    ciphertext = ''.join([char for char in ciphertext.upper() if char in string.ascii_uppercase])
    
    sequences = {}
    # Examiner des séquences de 3 caractères (trigrammes)
    for i in range(len(ciphertext) - 2):
        sequence = ciphertext[i:i+3]
        if sequence in sequences:
            sequences[sequence].append(i)
        else:
            sequences[sequence] = [i]

    # Calculer les distances entre les répétitions
    distances = []
    for sequence, positions in sequences.items():
        if len(positions) > 1:
            for i in range(1, len(positions)):
                distance = positions[i] - positions[i-1]
                distances.append(distance)

    return distances

def main():
    print("\n--- Kasiski Examination ---")
    user_input = input("Enter the ciphertext to perform Kasiski examination: ")
    
    # 1. Calcul des distances
    distances = kasiski_examination(user_input)
    
    if not distances:
        print("Aucune répétition de 3 lettres n'a été trouvée.")
        print("Essayez avec un texte plus long.")
        return

    print(f"Distances trouvées entre les répétitions : {distances}")

    # 2. Analyse des facteurs (pour deviner la longueur de la clé)
    all_potential_lengths = []
    for d in distances:
        all_potential_lengths.extend(get_factors(d))
    
    if all_potential_lengths:
        # On compte quel facteur (longueur de clé) revient le plus souvent
        counts = Counter(all_potential_lengths)
        most_common = counts.most_common(3)
        
        print("\n--- Analyse des résultats ---")
        print("Longueurs de clé les plus probables (basées sur les facteurs) :")
        for length, count in most_common:
            print(f"- Longueur {length} : trouvée {count} fois comme diviseur.")
    else:
        print("\nLes distances trouvées n'ont pas de petits diviseurs communs (2-12).")

if __name__ == "__main__":
    main()