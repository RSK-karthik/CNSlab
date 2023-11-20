from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
key=get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)
data=b"hello world!"
nonce = cipher.nonce
ciphertext=cipher.encrypt(data)
print("Cipher text: ",ciphertext)
decipher = AES.new(key,AES.MODE_EAX, nonce=nonce)
plaintext=decipher.decrypt(ciphertext)
print("Decrypted: ",plaintext.decode('utf-8'))
