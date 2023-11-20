from Crypto.Cipher import ARC4
from Crypto.Random import get_random_bytes
def encryption(key,plaintext):
    cipher=ARC4.new(key)
    ciphertext=cipher.encrypt(plaintext.encode('utf-8'))
    return ciphertext
def decryption(key,ciphertext):
    decipher=ARC4.new(key)
    plaintext=decipher.decrypt(ciphertext)
    return plaintext.decode('utf-8')
key=get_random_bytes(16)
plaintext = 'nen potha'
ciphertext=encryption(key,plaintext)
print("Ciphertext: ",ciphertext)
decryptedtext=decryption(key,ciphertext)
print("decrypted: ",decryptedtext)