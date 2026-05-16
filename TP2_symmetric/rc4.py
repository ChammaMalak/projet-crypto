# rc4.py
# Implémentation complète du chiffrement RC4

def ksa(key_bytes):
    """
    Key-Scheduling Algorithm (KSA)
    Initialise la permutation S de 0 à 255
    """
    S = list(range(256))
    j = 0
    key_len = len(key_bytes)
    
    for i in range(256):
        j = (j + S[i] + key_bytes[i % key_len]) & 0xFF
        S[i], S[j] = S[j], S[i]
    
    return S


def prga(S):
    """
    Pseudo-Random Generation Algorithm (PRGA)
    Génère le flux de clé (keystream) indéfiniment
    """
    i = 0
    j = 0
    while True:
        i = (i + 1) & 0xFF
        j = (j + S[i]) & 0xFF
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) & 0xFF]
        yield k


def rc4_logic(key_bytes, data_bytes):
    S = ksa(key_bytes)
    keystream = prga(S)
    result = bytes([b ^ next(keystream) for b in data_bytes])
    return result


def rc4_encrypt(key, plaintext):
    # Convertir la clé en bytes
    if isinstance(key, str):
        key_bytes = key.encode('utf-8')
    else:
        key_bytes = key
    
    # Convertir le texte clair en bytes
    if isinstance(plaintext, str):
        data_bytes = plaintext.encode('utf-8')
    else:
        data_bytes = plaintext
    
    return rc4_logic(key_bytes, data_bytes)


def rc4_decrypt(key, ciphertext):
    try:
        # Convertir la clé en bytes
        if isinstance(key, str):
            key_bytes = key.encode('utf-8')
        else:
            key_bytes = key
        
        # Convertir le ciphertext en bytes si c'est une chaîne hexadécimale
        if isinstance(ciphertext, str):
            byte_ciphertext = bytes.fromhex(ciphertext)
        else:
            byte_ciphertext = ciphertext
        
        # Appliquer RC4 (le XOR est réversible)
        decrypted_bytes = rc4_logic(key_bytes, byte_ciphertext)
        
        # Retourner le résultat décodé
        return decrypted_bytes.decode('utf-8', errors='replace')
    
    except ValueError as e:
        return f"Erreur: Format hexadécimal invalide - {str(e)}"
    except Exception as e:
        return f"Erreur lors du déchiffrement: {str(e)}"


# Fonction pour tester avec des données hexadécimales
def rc4_decrypt_hex(key, ciphertext_hex):
    return rc4_decrypt(key, ciphertext_hex)

