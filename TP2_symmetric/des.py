from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# DES key (must be exactly 8 bytes)
key = b'8bytekey'

def des_encrypt(plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plaintext.encode(), DES.block_size)
    ciphertext = cipher.encrypt(padded_text)
    return ciphertext

def des_decrypt(ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = unpad(cipher.decrypt(ciphertext), DES.block_size)
    return decrypted_text.decode()