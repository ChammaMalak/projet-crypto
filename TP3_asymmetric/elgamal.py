# elgamal_algo.py

import random

def power(a, b, p):
    result = 1
    a = a % p
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % p
        b = b >> 1
        a = (a * a) % p
    return result

def elgamal_keygen(p):
    g = random.randint(2, p - 2)
    x = random.randint(2, p - 2)  # private key
    y = power(g, x, p)            # public key
    return (p, g, y), x

def elgamal_encrypt(public_key, plaintext):
    p, g, y = public_key
    k = random.randint(2, p - 2)
    a = power(g, k, p)
    b = [(ord(char) * power(y, k, p)) % p for char in plaintext]
    return a, b

def elgamal_decrypt(private_key, a, b, p):
    s = power(a, private_key, p)
    s_inv = pow(s, -1, p)
    decrypted = [chr((char * s_inv) % p) for char in b]
    return ''.join(decrypted)

# Example usage
if __name__ == "__main__":
    p = 467
    public_key, private_key = elgamal_keygen(p)
    msg = "HELLO"

    a, b = elgamal_encrypt(public_key, msg)
    print("Encrypted:", (a, b))

    decrypted = elgamal_decrypt(private_key, a, b, p)
    print("Decrypted:", decrypted)
