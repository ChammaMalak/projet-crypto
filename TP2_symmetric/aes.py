from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# AES-128 key (must be 16 bytes)
key = b'16byteslongkey!!'

def aes_encrypt(plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_text = pad(plaintext.encode(), AES.block_size)
    ciphertext = cipher.encrypt(padded_text)
    return ciphertext

def aes_decrypt(ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted.decode()

# Example
if __name__ == "__main__":
    msg = "HelloAES"
    enc = aes_encrypt(msg)
    print("Encrypted:", enc)
    print("Decrypted:", aes_decrypt(enc))
