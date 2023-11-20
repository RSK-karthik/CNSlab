def encrypt(plain,key):
    ciper=''
    for i in range(len(plain)):
        if plain[i]==' ':
            ciper+=' '
            continue
        ciper+=chr((ord(plain[i])+ord(key[i])-2*97)%26+97)
    return ciper
def decrypt(cipher,key):
    plain=''
    for i in range(len(cipher)):
        if cipher[i]==' ':
            plain+=' '
            continue
        plain+=chr((ord(cipher[i])-ord(key[i]))%26+97)
    return plain
plaintext=input()
key=input()
cipher=encrypt(plaintext.lower(),key)
print('Encrypted text:',cipher)
print('Decrypted text:',decrypt(cipher.lower(),key))
