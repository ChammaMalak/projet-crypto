from Crypto.Util.number import getPrime, inverse, GCD
import hashlib

def generate_keys(bits=512):
    p = getPrime(bits)
    q = getPrime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537  # Standard
    if GCD(e, phi) != 1:
        e = 3
        while GCD(e, phi) != 1:
            e += 2

    d = inverse(e, phi)
    return (n, e, d)

def hash_message(message):
    h = hashlib.sha256()
    h.update(message.encode())
    return int(h.hexdigest(), 16)

def sign_message(message, d, n):
    hashed = hash_message(message)
    signature = pow(hashed, d, n)
    return signature

def verify_signature(message, signature, e, n):
    hashed = hash_message(message)
    check = pow(signature, e, n)
    return check == hashed
