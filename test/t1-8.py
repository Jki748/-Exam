from itertools import product

data = list((product("ADC", repeat = 3)))
k = 0
for i in data:
    w = ''.join(i)
    if i[1] == "A":
        k+=1

print(data)
print(k)