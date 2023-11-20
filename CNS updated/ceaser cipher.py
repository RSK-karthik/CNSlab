def encrypt(string,s):
    cipher=''
    for i in string:
        if i==' ':
            cipher+=' '
        elif i.isupper():
            cipher+=chr((ord(i)+s-65)%26+65)
        else:
            cipher+=chr((ord(i)+s-97)%26+97)
    return cipher
s=int(input("Enter the shift: "))
string=input("Enter the string: ")
cipher = encrypt(string,s)
print("The encrypted text is : ",cipher)
#for decryption just change the shift number sign to minus
print('The decrypted text is: ',encrypt(cipher,-s))