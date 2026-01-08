p = 23
q = 41
r = 7
d=0
answer = 0
while answer != 1:
    d+=1
    answer = (r*d) % ((p-1) * (q-1))

n = p*q
c = (30**7) % n
print(30**7)
# print(n)
decrypt = c^d % n
print(c^d)
print(n)
# print(decrypt)