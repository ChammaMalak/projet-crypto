import random
import Crypto.Util.number as num
import hashlib

def hash_message_to_int(message, p):
    h = hashlib.sha256()
    h.update(message.encode())
    hashed_int = int(h.hexdigest(), 16)
    return hashed_int % (p - 1)

def eg_key_generation(bits=256):
    p = num.getPrime(bits)
    alpha = random.randint(2, p - 2)
    x = random.randint(1, p - 2)  # clé privée
    y = pow(alpha, x, p)          # clé publique
    return p, alpha, x, y

def eg_sign(p, alpha, x, m):
    while True:
        k = random.randint(1, p - 2)
        if num.GCD(k, p - 1) == 1:
            break
    r = pow(alpha, k, p)
    k_inv = num.inverse(k, p - 1)
    s = (k_inv * (m - x * r)) % (p - 1)
    return r, s

def eg_verify(p, alpha, y, r, s, m):
    if not (1 <= r <= p - 1):
        return False
    v1 = (pow(y, r, p) * pow(r, s, p)) % p
    v2 = pow(alpha, m, p)
    return v1 == v2

# Fonctions haut niveau pour le menu
def sign_message(message, p, alpha, x):
    m_int = hash_message_to_int(message, p)
    return eg_sign(p, alpha, x, m_int)

def verify_signature(message, p, alpha, y, r, s):
    m_int = hash_message_to_int(message, p)
    return eg_verify(p, alpha, y, r, s, m_int)
