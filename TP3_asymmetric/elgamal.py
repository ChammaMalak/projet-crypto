import random

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

def elgamal_keygen(p):
    """Generates ElGamal public and private keys"""
    g = random.randint(2, p - 2)
    x = random.randint(2, p - 2)  # Private key
    y = power(g, x, p)            # Public key
    return (p, g, y), x

def elgamal_encrypt(public_key, plaintext):
    """Encrypts a plaintext message using ElGamal"""
    p, g, y = public_key
    k = random.randint(2, p - 2)
    a = power(g, k, p)
    b = [(ord(char) * power(y, k, p)) % p for char in plaintext]
    return a, b

def elgamal_decrypt(private_key, a, b, p):
    """Decrypts ciphertext (a, b) using ElGamal"""
    s = power(a, private_key, p)
    s_inv = pow(s, -1, p)
    decrypted = [chr((char * s_inv) % p) for char in b]
    return ''.join(decrypted)

def main():
    print("\n--- ElGamal Encryption/Decryption ---")

    p = 467  # Prime number
    msg = "HELLO"

    print(f"Original Message: {msg}")
    public_key, private_key = elgamal_keygen(p)

    print("\nKeys:")
    print("  Public Key:", public_key)
    print("  Private Key:", private_key)

    a, b = elgamal_encrypt(public_key, msg)
    print("\nEncrypted:")
    print("  a:", a)
    print("  b:", b)

    decrypted = elgamal_decrypt(private_key, a, b, p)
    print("\nDecrypted:")
    print(" ", decrypted)

if __name__ == "__main__":
    main()
