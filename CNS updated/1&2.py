s=input()
print('xor with 0')
for i in s:#1st
    print(chr(ord(i)^0),end='')
print('xor with 127')
for i in s:#2nd
    print(chr(ord(i)^127),end='')
print('and with 127')
for i in s:
    print(chr(ord(i)&127),end='')
print('or with 127')
for i in s:
    print(chr(ord(i)|127),end='')
