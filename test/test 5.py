# g = 0
# for k in range(100, 1000):
#     i = str(k)
#     r = int(i[0])+int(i[1])
#     r2 = int(i[1])+int(i[2])
#
#     q = str(max(r, r2))
#     q2 = str(min(r,r2))
#
#     ch = q2+q
#
#     if ch == "1216":
#         g+=1
#
# print(g)


k = 0
for i in range(100, 1000):

    a = str(i)

    w = int(a[0])+ int(a[1])
    w2 = int(a[1])+ int(a[2])

    fir = str(max(w, w2))
    sec = str(min(w, w2))

    res = fir + sec

    if res == "1715":
        k += 1

print(k)















