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

def diffie_hellman_key_exchange(p=23, g=5, a=6, b=15):
    """
    Simulates Diffie-Hellman key exchange.
    Returns (A, B, shared_key), where:
      - A: Alice's public key
      - B: Bob's public key
      - shared_key: the shared secret
    """
    A = power(g, a, p)  # Alice's public key
    B = power(g, b, p)  # Bob's public key
    shared_key_alice = power(B, a, p)
    shared_key_bob = power(A, b, p)
    assert shared_key_alice == shared_key_bob, "Keys do not match!"
    return A, B, shared_key_alice

def main():
    print("\n--- Diffie-Hellman Key Exchange ---")

    # You can switch to input() here if needed
    p = 23  # Prime number (public)
    g = 5   # Primitive root modulo p (public)

    a = 6   # Alice's private key
    b = 15  # Bob's private key

    print(f"Public values:\n  Prime (p) = {p}\n  Generator (g) = {g}")
    print(f"Private keys:\n  Alice (a) = {a}\n  Bob (b) = {b}")

    A, B, shared_key = diffie_hellman_key_exchange(p, g, a, b)

    print(f"Public keys:\n  Alice sends A = {A}\n  Bob sends B = {B}")
    print("Shared secret key:", shared_key)
    print("✅ Keys match. Secure communication possible.")

if __name__ == "__main__":
    main()
