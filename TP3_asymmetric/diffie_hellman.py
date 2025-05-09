# diffie_hellman.py

def power(a, b, p):
    result = 1
    a = a % p
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % p
        b = b >> 1
        a = (a * a) % p
    return result

# Example usage
if __name__ == "__main__":
    p = 23  # prime number
    g = 5   # primitive root modulo p

    a = 6   # Alice's private key
    b = 15  # Bob's private key

    A = power(g, a, p)  # Alice sends A
    B = power(g, b, p)  # Bob sends B

    shared_key_alice = power(B, a, p)
    shared_key_bob = power(A, b, p)

    print("Shared key (Alice):", shared_key_alice)
    print("Shared key (Bob):", shared_key_bob)
