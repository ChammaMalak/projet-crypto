from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# DES requires key to be 8 bytes
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

# Example
if __name__ == "__main__":
    message = "HelloDES"
    encrypted = des_encrypt(message)
    print("Encrypted:", encrypted)
    print("Decrypted:", des_decrypt(encrypted))
