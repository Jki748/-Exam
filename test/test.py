from itertools import product
from itertools import permutations
s = '0124'

data = [''.join(x) for x in product(s, repeat=4) ]
print(*data)


a = [''.join(x) for x in permutations(s, 4)]
print(*a)


r = [x for x in data if x[0] != '0']
print(*r)

print("")


pas = "0123456789"

k = [''.join(i) for i in product(pas, repeat=4)]
c = [''.join(i) for i in k if i[0] in "13" and i[1] in "02" and i[3] == "5" ]
print(len(k))
print(len(c))
print(*c)

d = "23 4 32"
t = d.split(" ")
print(t)
f = [''.join(i) for i in t]
print(f)


