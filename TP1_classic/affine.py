from math import gcd

def modinv(a, m):
    """Calcule l'inverse modulaire de a modulo m."""
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"Aucun inverse modulaire pour a={a} modulo {m}")

def affine_encrypt(plaintext, a, b):
    """Chiffre le texte clair avec le chiffrement affine."""
    if gcd(a, 26) != 1:
        raise ValueError("La clé 'a' doit être première avec 26.")
    plaintext = plaintext.upper().replace(" ", "")
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            x = ord(char) - ord('A')
            y = (a * x + b) % 26
            ciphertext += chr(y + ord('A'))
        else:
            ciphertext += char
    return ciphertext

def affine_decrypt(ciphertext, a, b):
    """Déchiffre le texte chiffré avec le chiffrement affine."""
    if gcd(a, 26) != 1:
        raise ValueError("La clé 'a' doit être première avec 26.")
    a_inv = modinv(a, 26)
    ciphertext = ciphertext.upper().replace(" ", "")
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            y = ord(char) - ord('A')
            x = (a_inv * (y - b)) % 26
            plaintext += chr(x + ord('A'))
        else:
            plaintext += char
    return plaintext

def affine_menu():
    while True:
        print("\n--- Affine Cipher ---")
        print("1. Encrypt message")
        print("2. Decrypt message")
        print("3. Find keys (Brute force)")
        print("4. Back to previous menu")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            plaintext = input("Enter the plaintext: ")
            while True:
                a = int(input("Enter the key 'a' (must be coprime with 26): "))
                if gcd(a, 26) == 1:
                    break
                print("Key 'a' must be coprime with 26. Please try again.")
            b = int(input("Enter the key 'b': "))
            encrypted = affine_encrypt(plaintext, a, b)
            print(f"Encrypted message: {encrypted}")

        elif choice == "2":
            ciphertext = input("Enter the ciphertext: ")
            while True:
                a = int(input("Enter the key 'a' (must be coprime with 26): "))
                if gcd(a, 26) == 1:
                    break
                print("Key 'a' must be coprime with 26. Please try again.")
            b = int(input("Enter the key 'b': "))
            decrypted = affine_decrypt(ciphertext, a, b)
            print(f"Decrypted message: {decrypted}")

        elif choice == "3":
            ciphertext = input("Enter the ciphertext: ")
            print("Note: Brute force may take some time if the ciphertext is long.")
            possible_decryptions = []
            for a in range(1, 26):
                if gcd(a, 26) == 1:
                    for b in range(26):
                        try:
                            decrypted = affine_decrypt(ciphertext, a, b)
                            possible_decryptions.append((a, b, decrypted))
                        except ValueError:
                            continue
            for a, b, decrypted in possible_decryptions:
                print(f"a = {a}, b = {b} -> Decrypted message: {decrypted}")

        elif choice == "4":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    affine_menu()
