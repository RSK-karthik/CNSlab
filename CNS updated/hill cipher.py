import numpy as np
def encrypt(plaintext,key):
    cipher=""
    if len(plaintext)%2:
        plaintext+='x'
    for i in range(0,len(plaintext),len(key)):
        pair=[]
        for j in range(len(key)):
            pair.append(ord(plaintext[i+j])-97)
        result = np.dot(key,pair)%26
        for j in range(len(key)):
            cipher += chr((result[j])+97)
    return cipher
def get_inverse_mod(a,m):
    for i in range(1,m):
        if (a*i)%m==1:
            return i
    return None
def decrypt(cipher,key):
    key=np.array(key)
    det=int(np.linalg.det(key))
    det = det%26
    inv_det=get_inverse_mod(det,26)
    print(inv_det)
    if inv_det is None:
        return ValueError("Key matrix is not invertible module 26")
    inverse_matrix = np.linalg.inv(key)
    adjoint_matrix = inverse_matrix * det * inv_det
    adjoint_matrix %= 26
    key=np.round(adjoint_matrix,0).astype(int)
    key %= 26
    decipher=''
    plain=''
    for i in range(0,len(cipher),len(key)):
        pair=[]
        for j in range(len(key)):
            pair.append(ord(cipher[i+j])-97)
        result = np.dot(key,pair)%26
        for j in range(len(key)):
            plain += chr((result[j])+97)
    return plain
keymatrix=[[3,2],[5,7]]
plaintext="avasaramaaa"
ciphertext=encrypt(plaintext,keymatrix)
print("cipher text:",ciphertext)
decrypted_text=decrypt(ciphertext,keymatrix)
print("decrypted: ",decrypted_text)