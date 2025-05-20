import hashlib

def hash_md5(message):
    return hashlib.md5(message.encode()).hexdigest()

def hash_sha1(message):
    return hashlib.sha1(message.encode()).hexdigest()

def hash_sha256(message):
    return hashlib.sha256(message.encode()).hexdigest()

def hash_sha3_256(message):
    return hashlib.sha3_256(message.encode()).hexdigest()

# Test rapide
if __name__ == "__main__":
    msg = input("Message à hacher: ")
    print("MD5       :", hash_md5(msg))
    print("SHA-1     :", hash_sha1(msg))
    print("SHA-256   :", hash_sha256(msg))
    print("SHA3-256  :", hash_sha3_256(msg))
