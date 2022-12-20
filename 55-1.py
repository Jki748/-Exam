def f(n):
    b = bin(n)[2:]
    if int(b) % 2 == 0:
        b = '10' + b[2:] + "0"
    else:
        b = '11' + b[2:] + "1"

    return int(b,2)

for i in range(10000):
    if f(i) > 16:
        print(i)
        break

