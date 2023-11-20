plain_text = "helloworld"
key = "head"
s = [i for i in key]
s.sort()
k1 = [s.index(i)+1 for i in key]
# print(k1)
l = len(k1)
t = []
idx = 0
while idx<len(plain_text):
    if idx+l>len(plain_text):
        t.append(list(plain_text[idx:]))
    else:
        t.append(list(plain_text[idx:idx+l]))
    idx+=l
if len(t[-1])<l:
    for i in range(l-len(t[-1])):
        t[-1].append("_")
# print(t)
tr = [["_" for i in range(len(t))]for j in range(len(t[0]))]
for i in range(len(tr)):
    for j in range(len(tr[0])):
        tr[i][j] = t[j][i]
# print(tr)
cipher = ""
for i in range(1,len(k1)+1):
    cipher+="".join(tr[k1.index(i)])
print(cipher)
print(t)
ans = ""
for i in t:
    ans+="".join(i)
print(ans)