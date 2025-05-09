from ast import main
from math import gcd

def affine_menu():
    from TP1_classic.cryptanalysis import affine

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
            encrypted = affine.affine_encrypt(plaintext, a, b)
            print(f"Encrypted message: {encrypted}")

        elif choice == "2":
            ciphertext = input("Enter the ciphertext: ")
            while True:
                a = int(input("Enter the key 'a' (must be coprime with 26): "))
                if gcd(a, 26) == 1:
                    break
                print("Key 'a' must be coprime with 26. Please try again.")
            b = int(input("Enter the key 'b': "))
            decrypted = affine.affine_decrypt(ciphertext, a, b)
            print(f"Decrypted message: {decrypted}")

        elif choice == "3":
            ciphertext = input("Enter the ciphertext: ")
            print("Note: Brute force may take some time if the ciphertext is long.")
            possible_decryptions = []
            for a in range(1, 26):
                if gcd(a, 26) == 1:
                    for b in range(26):
                        try:
                            decrypted = affine.affine_decrypt(ciphertext, a, b)
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
    main()
