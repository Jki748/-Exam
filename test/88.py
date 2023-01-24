from itertools import permutations

m = list(permutations("QWERTYUIOPASDFGHJKLZXCVBNM", 10))
m2 = []
t = "EUOAJ"
for i in m:
    d =''.join(i)
    m2.append(d)

print(m2)