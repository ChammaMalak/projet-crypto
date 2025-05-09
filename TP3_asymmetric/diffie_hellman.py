def power(a, b, p):
    """Modular exponentiation: (a^b) % p"""
    result = 1
    a = a % p
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % p
        b = b >> 1
        a = (a * a) % p
    return result

def main():
    print("\n--- Diffie-Hellman Key Exchange ---")

    # You can switch to input() here if needed
    p = 23  # Prime number (public)
    g = 5   # Primitive root modulo p (public)

    a = 6   # Alice's private key
    b = 15  # Bob's private key

    print(f"Public values:\n  Prime (p) = {p}\n  Generator (g) = {g}")
    print(f"Private keys:\n  Alice (a) = {a}\n  Bob (b) = {b}")

    A = power(g, a, p)  # Alice's public key
    B = power(g, b, p)  # Bob's public key

    print(f"Public keys:\n  Alice sends A = {A}\n  Bob sends B = {B}")

    shared_key_alice = power(B, a, p)
    shared_key_bob = power(A, b, p)

    print("Shared secret key computed by Alice:", shared_key_alice)
    print("Shared secret key computed by Bob:", shared_key_bob)

    if shared_key_alice == shared_key_bob:
        print("✅ Keys match. Secure communication possible.")
    else:
        print("❌ Keys do not match. Something went wrong.")

if __name__ == "__main__":
    main()
def power(a, b, p):
    """Modular exponentiation: (a^b) % p"""
    result = 1
    a = a % p
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % p
        b = b >> 1
        a = (a * a) % p
    return result

def main():
    print("\n--- Diffie-Hellman Key Exchange ---")

    # You can switch to input() here if needed
    p = 23  # Prime number (public)
    g = 5   # Primitive root modulo p (public)

    a = 6   # Alice's private key
    b = 15  # Bob's private key

    print(f"Public values:\n  Prime (p) = {p}\n  Generator (g) = {g}")
    print(f"Private keys:\n  Alice (a) = {a}\n  Bob (b) = {b}")

    A = power(g, a, p)  # Alice's public key
    B = power(g, b, p)  # Bob's public key

    print(f"Public keys:\n  Alice sends A = {A}\n  Bob sends B = {B}")

    shared_key_alice = power(B, a, p)
    shared_key_bob = power(A, b, p)

    print("Shared secret key computed by Alice:", shared_key_alice)
    print("Shared secret key computed by Bob:", shared_key_bob)

    if shared_key_alice == shared_key_bob:
        print("✅ Keys match. Secure communication possible.")
    else:
        print("❌ Keys do not match. Something went wrong.")

if __name__ == "__main__":
    main()
