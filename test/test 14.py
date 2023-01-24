a = 49**10 + 7**30 - 49
k = 0
while a > 0:
    c = a%7
    if c == 6:
        k+=1
    a = a // 7

print(k)
