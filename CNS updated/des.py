from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad,unpad
def encryption(plain,key):
    cipher = DES.new(key,DES.MODE_ECB)
    padded_text = pad(plain,DES.block_size)
    encrypted=cipher.encrypt(padded_text)
    return encrypted
def decryption(cipher,key):
    decipher=DES.new(key,DES.MODE_ECB)
    unpadded=decipher.decrypt(cipher)
    decrypted=unpad(unpadded,DES.block_size)
    return decrypted
key=get_random_bytes(8)
plaintext=b"hello world"
ciphertext=encryption(plaintext,key)
print('encrypted text:', ciphertext,'\n') 
decrypted=decryption(ciphertext,key)
print("decrypted text: ",decrypted.decode('utf-8'))