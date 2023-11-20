import math
def gcd(a,h):
    while h:
        a,h=h,a%h
    return a
p=7
q=11
n=p*q
phi=(p-1)*(q-1)
e=2
d=2
while e<phi:
    if gcd(e,phi)==1:
        break
    e+=1
while d<phi:
    if (((d*e)%phi)==1):
        break
    d+=1
print(e,n)
print(d,n)
msg=75
print(msg)
c=(msg**e)%n
print(c)
m=(c**d)%n
print(m)