def f(n):
    ch = bin(n)[2:]
    if int(ch.count('0') + ch.count('1')) % 2 == 0:
        ch = ch + "10"
    if int(ch.count('0') + ch.count('1')) % 2 != 0:
        ch = ch + "11"

    return int(ch,2)
c = 0
m = []
for i in range(100, 201):
    m.append(f(i))

for j in range(len(m)):
    if f(m[j]) % 2 == 0:
        c+=1

print(c)

