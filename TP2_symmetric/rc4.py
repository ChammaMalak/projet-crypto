# RC4 stream cipher implementation

def ksa(key):
    """Key Scheduling Algorithm (KSA)"""
    key_length = len(key)
    S = list(range(256))
    j = 0

    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]

    return S

def prga(S):
    """Pseudo-Random Generation Algorithm (PRGA)"""
    i = j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        yield S[(S[i] + S[j]) % 256]

def rc4(key, plaintext):
    """RC4 encryption/decryption"""
    key = [ord(c) for c in key]
    S = ksa(key)
    keystream = prga(S)
    return ''.join([chr(ord(c) ^ next(keystream)) for c in plaintext])

# Example
if __name__ == "__main__":
    key = "secret"
    text = "hello"
    cipher = rc4(key, text)
    print("Encrypted:", cipher)
    print("Decrypted:", rc4(key, cipher))  # Symmetric
