"""
Analyse de fréquence des lettres dans un texte chiffré.
Cette méthode est utilisée pour casser les chiffres mono-alphabétiques comme César et Substitution.
"""

import string
from collections import Counter

# Fréquence des lettres en anglais (approximative)
ENGLISH_FREQUENCY = {
    'E': 12.02, 'T': 9.10, 'A': 8.12, 'O': 7.68, 'I': 7.31, 'N': 6.95, 'S': 6.28, 'R': 6.02, 'H': 5.92, 'D': 4.32,
    'L': 3.98, 'U': 2.88, 'C': 2.71, 'M': 2.61, 'F': 2.30, 'Y': 2.11, 'W': 2.09, 'G': 2.03, 'P': 1.82, 'B': 1.49,
    'V': 1.11, 'K': 0.69, 'X': 0.17, 'Q': 0.11, 'J': 0.10, 'Z': 0.07
}

def analyze_frequency(ciphertext):
    """
    Analyse la fréquence des lettres dans un texte chiffré et compare avec la fréquence attendue en anglais.
    """
    ciphertext = ''.join([char for char in ciphertext.upper() if char in string.ascii_uppercase])
    letter_counts = Counter(ciphertext)
    total_letters = sum(letter_counts.values())
    if total_letters == 0:
        return {}
    frequencies = {char: letter_counts[char] / total_letters * 100 for char in letter_counts}
    return frequencies

def frequency_analysis(text):
    return analyze_frequency(text)

def compare_frequency(frequencies):
    """
    Compare les fréquences analysées avec les fréquences de l'anglais.
    Plus la différence est faible, plus le texte est probable d'être chiffré de manière mono-alphabétique.
    """
    # Calculer la différence entre les fréquences analysées et les fréquences standard
    diff = 0
    for char, freq in frequencies.items():
        if char in ENGLISH_FREQUENCY:
            diff += abs(freq - ENGLISH_FREQUENCY[char])
    
    return diff

def main():
    print("\n--- Frequency Analysis ---")
    ciphertext = input("Enter the ciphertext to analyze: ")
    
    # Analyse de la fréquence
    frequencies = analyze_frequency(ciphertext)
    print(f"Fréquences analysées : {frequencies}")
    
    # Comparaison avec les fréquences anglaises
    diff = compare_frequency(frequencies)
    print(f"Différence avec la fréquence anglaise : {diff}")
    
    # Déterminer si le texte est probablement chiffré avec un chiffre mono-alphabétique
    if diff < 5:  # Seuil arbitraire pour déterminer si le texte est probablement chiffré de manière mono-alphabétique
        print("Le texte est probablement chiffré avec un chiffre mono-alphabétique.")
    else:
        print("Le texte n'est probablement pas chiffré avec un chiffre mono-alphabétique.")

# Exemple d'utilisation (sera ignoré si le module est importé)
if __name__ == "__main__":
    main()
