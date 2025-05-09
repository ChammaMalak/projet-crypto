from ast import main


def caesar_encrypt(plaintext, shift):
    """Chiffre le texte clair avec le chiffrement de César."""
    plaintext = plaintext.upper()
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            x = ord(char) - ord('A')
            y = (x + shift) % 26
            ciphertext += chr(y + ord('A'))
        else:
            ciphertext += char
    return ciphertext

def caesar_decrypt(ciphertext, shift):
    """Déchiffre le texte chiffré avec le chiffrement de César."""
    ciphertext = ciphertext.upper()
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            y = ord(char) - ord('A')
            x = (y - shift) % 26
            plaintext += chr(x + ord('A'))
        else:
            plaintext += char
    return plaintext


def caesar_menu():
    from TP1_classic.cryptanalysis import cesar

    while True:
        print("\n--- Caesar Cipher ---")
        print("1. Encrypt message")
        print("2. Decrypt message")
        print("3. Back to previous menu")
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            plaintext = input("Enter the plaintext: ")
            while True:
                try:
                    shift = int(input("Enter the shift value (1-25): "))
                    if 1 <= shift <= 25:
                        break
                    else:
                        print("Shift value must be between 1 and 25. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a valid integer for the shift value.")
            encrypted = caesar_encrypt(plaintext, shift)
            print(f"Encrypted message: {encrypted}")

        elif choice == "2":
            ciphertext = input("Enter the ciphertext: ")
            while True:
                try:
                    shift = int(input("Enter the shift value (1-25): "))
                    if 1 <= shift <= 25:
                        break
                    else:
                        print("Shift value must be between 1 and 25. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a valid integer for the shift value.")
            decrypted = caesar_decrypt(ciphertext, shift)
            print(f"Decrypted message: {decrypted}")

        elif choice == "3":
            break

        else:
            print("Invalid option. Please try again.")
if __name__ == "__main__":
    main()
