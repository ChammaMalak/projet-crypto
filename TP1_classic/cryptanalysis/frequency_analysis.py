import string
from collections import Counter

# Fréquences des lettres anglaises
ENGLISH_FREQUENCY = {
    'E': 12.02, 'T': 9.10, 'A': 8.12, 'O': 7.68,
    'I': 7.31, 'N': 6.95, 'S': 6.28, 'R': 6.02,
    'H': 5.92, 'D': 4.32, 'L': 3.98, 'U': 2.88,
    'C': 2.71, 'M': 2.61, 'F': 2.30, 'Y': 2.11,
    'W': 2.09, 'G': 2.03, 'P': 1.82, 'B': 1.49,
    'V': 1.11, 'K': 0.69, 'X': 0.17, 'Q': 0.11,
    'J': 0.10, 'Z': 0.07
}


def clean_text(text):
    """
    Garde uniquement les lettres A-Z.
    """

    return ''.join(
        char for char in text.upper()
        if char in string.ascii_uppercase
    )


def analyze_frequency(text):
    """
    Analyse les fréquences des lettres.
    """

    text = clean_text(text)

    counts = Counter(text)

    total = sum(counts.values())

    frequencies = {}

    for letter in string.ascii_uppercase:
        frequencies[letter] = (
            counts.get(letter, 0) / total * 100
        ) if total > 0 else 0

    return frequencies, total


def compare_frequency(frequencies):
    """
    Compare les fréquences observées avec l'anglais.
    """

    diff = 0

    for letter in string.ascii_uppercase:
        observed = frequencies.get(letter, 0)
        expected = ENGLISH_FREQUENCY.get(letter, 0)

        diff += abs(observed - expected)

    return diff


def print_frequencies(frequencies):

    print("\n--- Fréquences des lettres ---")

    sorted_freq = sorted(
        frequencies.items(),
        key=lambda x: x[1],
        reverse=True
    )

    for letter, freq in sorted_freq:

        if freq > 0:
            print(f"{letter} : {freq:.2f}%")


def main():

    print("\n--- Frequency Analysis ---")

    ciphertext = input("Enter the ciphertext to analyze: ")

    frequencies, total = analyze_frequency(ciphertext)

    if total == 0:
        print("Aucune lettre détectée.")
        return

    print(f"\nNombre total de lettres : {total}")

    print_frequencies(frequencies)

    diff = compare_frequency(frequencies)

    print(f"\nDifférence avec l'anglais : {diff:.2f}")

    # Analyse intelligente

    if total < 30:

        print("\n⚠ Texte trop court pour une analyse fiable.")
        print("Impossible de conclure avec précision.")

    else:

        if diff < 60:
            print("\n✓ Le texte pourrait être mono-alphabétique.")
        else:
            print("\n✗ Le texte ne ressemble pas à un texte anglais classique.")


if __name__ == "__main__":
    main()