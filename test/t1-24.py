f = open("t1-24.txt")

data = f.read().strip()

sogl = 'BCDF'
gl = "AEU"
maxim = 0
cur = 0

for i in range(2, len(data)-2, 3):
    if (data[i] in sogl) and (data[i+1] in gl) and (data[i+2] in sogl):
        cur += 1
        maxim = max(cur, maxim)
    else:
        cur = 0

print(maxim)