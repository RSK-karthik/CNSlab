def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
a=10
b=40
print(gcd(a,b))
def gcdExtended(a,b):
    if a==0:
        return b,0,1
    gcd,x1,y1=gcdExtended(b%a,a)
    x=y1-(b//a)*x1
    y=x1
    return gcd,x,y
a=10
b=40
print(gcdExtended(a,b))