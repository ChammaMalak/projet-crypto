import importlib

# TP1 - Classical Ciphers
from TP1_classic import affine, cesar, hill, otp, playfair, substitution, vigenere
from TP1_classic.cryptanalysis import frequency_analysis, index_of_coincidence, kasiski

# TP2 - Symmetric Ciphers
from TP2_symmetric import aes, des, rc4

# TP3 - Asymmetric Ciphers
from TP3_asymmetric import diffie_hellman, elgamal, rsa

def main():
    while True:
        print("\n=== Crypto Project Menu ===")
        print("1. Classical Algorithms")
        print("2. Symmetric Algorithms")
        print("3. Asymmetric Algorithms")
        print("0. Exit")
        choice = input("Choose a category: ")

        if choice == '1':
            classical_menu()
        elif choice == '2':
            symmetric_menu()
        elif choice == '3':
            asymmetric_menu()
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

def classical_menu():
    print("\n-- Classical Algorithms --")
    options = {
        '1': "affine",
        '2': "cesar",
        '3': "hill",
        '4': "otp",
        '5': "playfair",
        '6': "substitution",
        '7': "vigenere",
        '8': "cryptanalysis.frequency_analysis",
        '9': "cryptanalysis.index_of_coincidence",
        '10': "cryptanalysis.kasiski"
    }

    for key, val in options.items():
        print(f"{key}. {val.replace('_', ' ').title()}")

    choice = input("Choose an algorithm: ")
    if choice in options:
        run_module(f"TP1_classic.{options[choice]}")
    else:
        print("Invalid choice.")

def symmetric_menu():
    print("\n-- Symmetric Algorithms --")
    options = {
        '1': "aes",
        '2': "des",
        '3': "rc4",
        '4': "aes_finalists.serpent",
        '5': "aes_finalists.twofish"
    }

    for key, val in options.items():
        print(f"{key}. {val.upper()}")

    choice = input("Choose an algorithm: ")
    if choice in options:
        run_module(f"TP2_symmetric.{options[choice]}")
    else:
        print("Invalid choice.")

def asymmetric_menu():
    print("\n-- Asymmetric Algorithms --")
    options = {
        '1': "diffie_hellman",
        '2': "elgamal",
        '3': "rsa"
    }

    for key, val in options.items():
        print(f"{key}. {val.upper()}")

    choice = input("Choose an algorithm: ")
    if choice in options:
        run_module(f"TP3_asymmetric.{options[choice]}")
    else:
        print("Invalid choice.")

def run_module(module_path):
    try:
        # Dynamically import the module using its path
        module = importlib.import_module(module_path)

        # Check if the module has a 'main' function and run it
        if hasattr(module, "main"):
            print(f"Running module: {module_path}")
            module.main()  # Call the main function inside the module
        else:
            print(f"Module '{module_path}' has no 'main()' function.")
    except ModuleNotFoundError:
        print(f"Module '{module_path}' not found.")
    except Exception as e:
        print(f"Error running module: {e}")

if __name__ == "__main__":
    main()
    