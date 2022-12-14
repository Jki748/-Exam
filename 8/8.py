
from itertools import product
s = '0123456789ABCDEF'

data = [''.join(x) for x in product(s, repeat=5)]
data = [x for x in data if x[0] != '0']

k = 0
for x in data:
   flag = True
   for d in range(4):
       if x[d] > x[d + 1]:
           flag = False
           break
   if flag:
       k += 1
print(k)