def f(n):
    ch = bin(n)[2:]
    sum1 = sum(map(int,str(n)))

    if sum1 % 2 != 0:
        ch = ch + '1'
    else:
        ch = ch + '0'

    dec_ch = int(ch,2)
    sum1 = sum(map(int,str(dec_ch)))
    if sum1 % 2 != 0:
        ch = ch + '1'
    else:
        ch = ch + '0'

    dec_ch = int(ch, 2)
    sum1 = sum(map(int, str(dec_ch)))
    if sum1 % 2 != 0:
        ch = ch + '1'
    else:
        ch = ch + '0'

    return (int(ch, 2))


m = []
for i in range(10000):
    if f(i) > 2054:
        m.append(f(i))

print(m[0])






