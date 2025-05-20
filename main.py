import importlib
import numpy as np
# TP1 - Classical Ciphers
from TP1_classic import affine, cesar, hill, otp, playfair, substitution, vigenere
from TP1_classic.cryptanalysis import frequency_analysis, index_of_coincidence, kasiski

# TP2 - Symmetric Ciphers
from TP2_symmetric import aes, des, rc4

# TP3 - Asymmetric Ciphers
from TP3_asymmetric import diffie_hellman, elgamal, rsa

# TP4 - Signatures and Hash Functions
import hashlib
from TP4_hash_and_signature import signature_rsa, signature_elgamal

def main():
    while True:
        print("\n=== Crypto Project Menu ===")
        print("1. Classical Algorithms")
        print("2. Symmetric Algorithms")
        print("3. Asymmetric Algorithms")
        print("4. Signatures")
        print("5. Hash Functions")
        print("0. Exit")
        choice = input("Choose a category: ")

        if choice == '1':
            classical_menu()
        elif choice == '2':
            symmetric_menu()
        elif choice == '3':
            asymmetric_menu()
        elif choice == '4':
            signature_menu()
        elif choice == '5':
            hash_menu()
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

def signature_menu():
    print("\n-- Signature Menu --")
    print("1. RSA Signature")
    print("2. ElGamal Signature")
    choice = input("Choose signature method: ")

    msg = input("Enter the message to sign: ")

    if choice == '1':
        try:
            # Génération des clés RSA (n, e, d)
            n, e, d = signature_rsa.generate_keys()
            signature = signature_rsa.sign_message(msg, d, n)
            print(f"Signature (RSA): {signature}")
            valid = signature_rsa.verify_signature(msg, signature, e, n)
            print(f"Signature verification: {'valid' if valid else 'invalid'}")
        except Exception as e:
            print("RSA signature error:", e)

    elif choice == '2':
        try:
            # Génération des clés ElGamal (p, alpha, x, y)
            p, alpha, x, y = signature_elgamal.eg_key_generation()
            signature = signature_elgamal.sign_message(msg, p, alpha, x)  # signature = (r, s)
            print(f"Signature (ElGamal): r={signature[0]}, s={signature[1]}")
            valid = signature_elgamal.verify_signature(msg, p, alpha, y, signature[0], signature[1])
            print(f"Signature verification: {'valid' if valid else 'invalid'}")
        except Exception as e:
            print("ElGamal signature error:", e)
    else:
        print("Invalid choice.")

def hash_menu():
    print("\n-- Hash Functions Menu --")
    print("1. MD5")
    print("2. SHA1")
    print("3. SHA256")
    print("4. SHA3_256")
    choice = input("Choose hash function: ")
    msg = input("Enter the message to hash: ").encode()

    if choice == '1':
        h = hashlib.md5(msg).hexdigest()
    elif choice == '2':
        h = hashlib.sha1(msg).hexdigest()
    elif choice == '3':
        h = hashlib.sha256(msg).hexdigest()
    elif choice == '4':
        h = hashlib.sha3_256(msg).hexdigest()
    else:
        print("Invalid choice.")
        return

    print(f"Hash: {h}")

def classical_menu():
    print("\n-- Classical Algorithms --")
    options = {
        '1': ("Affine", affine),
        '2': ("Cesar", cesar),
        '3': ("Hill", hill),
        '4': ("OTP", otp),
        '5': ("Playfair", playfair),
        '6': ("Substitution", substitution),
        '7': ("Vigenere", vigenere),
        '8': ("Frequency Analysis", frequency_analysis),
        '9': ("Index of Coincidence", index_of_coincidence),
        '10': ("Kasiski", kasiski)
    }

    for key, (name, _) in options.items():
        print(f"{key}. {name}")

    choice = input("Choose an algorithm: ")
    if choice in options:
        name, module = options[choice]
        if name == "Affine":
            affine_menu()
        elif name == "Cesar":
            cesar_menu()
        elif name == "Hill":
            hill_menu()
        elif name == "OTP":
            otp_menu()
        elif name == "Playfair":
            playfair_menu()
        elif name == "Substitution":
            substitution_menu()
        elif name == "Vigenere":
            vigenere_menu()
        elif name in ["Frequency Analysis", "Index of Coincidence", "Kasiski"]:
            if hasattr(module, "main"):
                module.main()
            else:
                print(f"{name} does not have a main() function.")
        else:
            print(f"Module for {name} not implemented in this menu.")
    else:
        print("Invalid choice.")

def affine_menu():
    print("\n-- Affine Cipher --")
    action = input("Encrypt (e) or Decrypt (d)? ").lower()
    if action in ['e', 'd']:
        text = input("Enter text: ")
        while True:
            try:
                a = int(input("Enter key 'a' (coprime with 26, integer): "))
                break
            except ValueError:
                print("Key 'a' must be an integer. Please try again.")
        while True:
            try:
                b = int(input("Enter key 'b' (integer): "))
                break
            except ValueError:
                print("Key 'b' must be an integer. Please try again.")
        try:
            if action == 'e':
                result = affine.affine_encrypt(text, a, b)
                print(f"Ciphertext: {result}")
            else:
                result = affine.affine_decrypt(text, a, b)
                print(f"Plaintext: {result}")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Invalid action.")

def cesar_menu():
    print("\n-- Cesar Cipher --")
    action = input("Encrypt (e) or Decrypt (d)? ").lower()
    if action in ['e', 'd']:
        text = input("Enter text: ")
        while True:
            try:
                key = int(input("Enter key (integer): "))
                break
            except ValueError:
                print("Key must be an integer. Please try again.")
        try:
            if action == 'e':
                result = cesar.cesar_encrypt(text, key)
                print(f"Ciphertext: {result}")
            else:
                result = cesar.cesar_decrypt(text, key)
                print(f"Plaintext: {result}")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Invalid action.")

def otp_menu():
    print("\n-- OTP Cipher --")
    action = input("Encrypt (e) or Decrypt (d)? ").lower()
    if action == 'e':
        text = input("Enter plaintext: ")
        ciphertext, key = otp.otp_encrypt(text)
        print(f"Ciphertext: {ciphertext}")
        print(f"Key: {key}")
    elif action == 'd':
        ciphertext = input("Enter ciphertext: ")
        key = input("Enter key: ")
        result = otp.otp_decrypt(ciphertext, key)
        print(f"Plaintext: {result}")
    else:
        print("Invalid action.")

def playfair_menu():
    print("\n-- Playfair Cipher --")
    action = input("Encrypt (e) or Decrypt (d)? ").lower()
    key = input("Enter key (default MONARCHY): ") or "MONARCHY"
    if action == 'e':
        text = input("Enter plaintext: ")
        result = playfair.playfair_encrypt(text, key)
        print(f"Ciphertext: {result}")
    elif action == 'd':
        ciphertext = input("Enter ciphertext: ")
        result = playfair.playfair_decrypt(ciphertext, key)
        print(f"Plaintext: {result}")
    else:
        print("Invalid action.")

def substitution_menu():
    print("\n-- Substitution Cipher --")
    action = input("Encrypt (e) or Decrypt (d)? ").lower()
    if action == 'e':
        text = input("Enter plaintext: ")
        key = substitution.generate_random_alphabet()
        print(f"Random key used: {key}")
        result = substitution.substitution_encrypt(text, key)
        print(f"Ciphertext: {result}")
    elif action == 'd':
        ciphertext = input("Enter ciphertext: ")
        key = input("Enter key (26-letter permutation): ")
        try:
            substitution.validate_key(key)
            result = substitution.substitution_decrypt(ciphertext, key)
            print(f"Plaintext: {result}")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Invalid action.")

def vigenere_menu():
    print("\n-- Vigenere Cipher --")
    action = input("Encrypt (e) or Decrypt (d)? ").lower()
    key = input("Enter key (letters only): ")
    if action == 'e':
        text = input("Enter plaintext: ")
        try:
            result = vigenere.vigenere_encrypt(text, key)
            print(f"Ciphertext: {result}")
        except Exception as e:
            print(f"Error: {e}")
    elif action == 'd':
        ciphertext = input("Enter ciphertext: ")
        try:
            result = vigenere.vigenere_decrypt(ciphertext, key)
            print(f"Plaintext: {result}")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Invalid action.")

def hill_menu():
    print("\n-- Hill Cipher --")
    action = input("Encrypt (e) or Decrypt (d)? ").lower()
    if action == 'e':
        message = input("Enter plaintext: ")
        try:
            result = hill.hill_encrypt(message)
            print(f"Ciphertext: {result}")
        except Exception as e:
            print(f"Error: {e}")
    elif action == 'd':
        ciphertext = input("Enter ciphertext: ")
        try:
            result = hill.hill_decrypt(ciphertext)
            print(f"Plaintext: {result}")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Invalid action.")

def symmetric_menu():
    print("\n-- Symmetric Algorithms --")
    options = {
        '1': ("AES", aes),
        '2': ("DES", des),
        '3': ("RC4", rc4)
    }
    for key, (name, _) in options.items():
        print(f"{key}. {name}")
    choice = input("Choose an algorithm: ")
    if choice == '1':
        print("\n--- AES (ECB mode) ---")
        action = input("Encrypt (e) or Decrypt (d)? ").lower()
        if action == 'e':
            plaintext = input("Enter the plaintext: ")
            encrypted = aes.aes_encrypt(plaintext)
            print("Encrypted (hex):", encrypted.hex())
        elif action == 'd':
            hex_input = input("Enter the ciphertext (hex): ")
            try:
                ciphertext = bytes.fromhex(hex_input)
                decrypted = aes.aes_decrypt(ciphertext)
                print("Decrypted text:", decrypted)
            except Exception as e:
                print("Decryption failed:", e)
        else:
            print("Invalid option.")
    elif choice == '2':
        print("\n--- DES (ECB mode) ---")
        action = input("Encrypt (e) or Decrypt (d)? ").lower()
        if action == 'e':
            plaintext = input("Enter the plaintext: ")
            encrypted = des.des_encrypt(plaintext)
            print("Encrypted (hex):", encrypted.hex())
        elif action == 'd':
            hex_input = input("Enter the ciphertext (hex): ")
            try:
                ciphertext = bytes.fromhex(hex_input)
                decrypted = des.des_decrypt(ciphertext)
                print("Decrypted text:", decrypted)
            except Exception as e:
                print("Decryption failed:", e)
        else:
            print("Invalid option.")
    elif choice == '3':
        print("\n--- RC4 Stream Cipher ---")
        action = input("Encrypt (e) or Decrypt (d)? ").lower()
        key = input("Enter the key: ")
        if action == 'e':
            plaintext = input("Enter the plaintext: ")
            encrypted = rc4.rc4_encrypt(key, plaintext)
            print("Encrypted (hex):", encrypted.hex())
        elif action == 'd':
            hex_input = input("Enter the ciphertext (hex): ")
            try:
                ciphertext = bytes.fromhex(hex_input)
                decrypted = rc4.rc4_decrypt(key, ciphertext)
                print("Decrypted text:", decrypted.decode('latin1'))
            except Exception as e:
                print("Decryption failed:", e)
        else:
            print("Invalid option.")
    else:
        print("Invalid choice.")

def asymmetric_menu():
    print("\n-- Asymmetric Algorithms --")
    options = {
        '1': ("Diffie-Hellman", diffie_hellman),
        '2': ("ElGamal", elgamal),
        '3': ("RSA", rsa)
    }
    for key, (name, _) in options.items():
        print(f"{key}. {name}")
    choice = input("Choose an algorithm: ")
    if choice == '1':
        print("\n--- Diffie-Hellman Key Exchange ---")
        try:
            p = int(input("Enter prime p (default 23): ") or "23")
            g = int(input("Enter generator g (default 5): ") or "5")
            a = int(input("Enter Alice's private key a (default 6): ") or "6")
            b = int(input("Enter Bob's private key b (default 15): ") or "15")
            A, B, shared = diffie_hellman.diffie_hellman_key_exchange(p, g, a, b)
            print(f"Alice's public key: {A}")
            print(f"Bob's public key: {B}")
            print(f"Shared secret: {shared}")
        except Exception as e:
            print("Error:", e)
    elif choice == '2':
        print("\n--- ElGamal Encryption/Decryption ---")
        try:
            p = int(input("Enter prime p (default 467): ") or "467")
            msg = input("Enter message: ")
            public_key, private_key = elgamal.elgamal_keygen(p)
            print("Public Key:", public_key)
            print("Private Key:", private_key)
            a, b = elgamal.elgamal_encrypt(public_key, msg)
            print("Encrypted a:", a)
            print("Encrypted b:", b)
            decrypted = elgamal.elgamal_decrypt(private_key, a, b, p)
            print("Decrypted:", decrypted)
        except Exception as e:
            print("Error:", e)
    elif choice == '3':
        print("\n--- RSA Encryption/Decryption ---")
        try:
            p = int(input("Enter prime p (default 61): ") or "61")
            q = int(input("Enter prime q (default 53): ") or "53")
            public, private = rsa.generate_keypair(p, q)
            print("Public Key:", public)
            print("Private Key:", private)
            msg = input("Enter message: ")
            encrypted = rsa.encrypt(public, msg)
            print("Encrypted:", encrypted)
            decrypted = rsa.decrypt(private, encrypted)
            print("Decrypted:", decrypted)
        except Exception as e:
            print("Error:", e)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
