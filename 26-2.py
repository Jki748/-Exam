import math
n = int(input())
f = list(map(int, input().split()))
a = []
#сумма товаров со скидкой:
sum1 = 0
maxc = 0
razmer_skidki = 0

for i in f:
    x = int(i)
    if x <= 100:
        sum1 +=x
    else:
        a.append(x)
a.sort
for i in range(len(a)):
    if i < len(a)//2:
        sum1+= a[i]*0.7
        razmer_skidki += a[i]*0.3
        maxc = a[i]
    else:
        sum1+=a[i]

print(math.floor(razmer_skidki), maxc)




