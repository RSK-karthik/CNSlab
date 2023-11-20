#deffie hellman
import math
#check for prime 
def prime(n):
    if n==1:
        return False
    if n==2 or n==3:
        return True
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
q = int(input())
if not prime(q):
    print("Enter a prime number!!!")
#primtive root
def primitive(n):
    for i in range(1,n):
        x=i
        s = set()
        for j in range(1,n):
            s.add(math.fmod(x**j,n))
        if len(s)==n-1:
            return x
    return -1
print(primitive(q))
alpha = primitive(q)
#public key of A
Xa = 3
Ya = math.fmod(alpha**Xa,q)
#public key of B
Xb = 5
Yb = math.fmod(alpha**Xb,q)
#secret keys
ka = math.fmod(Yb**Xa,q) 
kb = math.fmod(Ya**Xb,q)
print(ka,kb)
