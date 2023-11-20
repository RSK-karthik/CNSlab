from Crypto.Cipher import Blowfish
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
def encryption(key,plaintext):
    cipher = Blowfish.new(key,Blowfish.MODE_ECB)
    padded_text = pad(plaintext,Blowfish.block_size)
    ciphertext=cipher.encrypt(padded_text)
    return ciphertext
def decryption(key,ciphertext):
    decipher=Blowfish.new(key,Blowfish.MODE_ECB)
    unpadded=decipher.decrypt(ciphertext)
    decrypted = unpad(unpadded,Blowfish.block_size)
    return decrypted
key = get_random_bytes(8)
plaintext=b'endhi bro idhi'
encrypted_text=encryption(key,plaintext)
print('Encrypted text: ', encrypted_text,'\n')
decrypted_text=decryption(key,encrypted_text)
print('Decrypted text:', decrypted_text.decode('utf-8'))
