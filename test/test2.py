# ¬y ∨ (x ∧ ¬z)
# print ("x y z")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             if (not y) or (x and (not z)) == True:
#                 print(x, y, z)




# s = 22
# n = 0
# while s < s*s:
#     s = s - 1
#     n = n + 3
# print(n)


#dont work
# def f (x):
#     c = str(x)
#     d = int(c[0])+int(c[1])
#     d1 = int(c[2])+int(c[3])
#
#     if d > d1:
#         lol = str(d)+str(d1)
#         return lol
#     if d < d1:
#         lol = str(d1)+ str(d)
#         return lol
#
# c = 0
# for i in range(1000, 1000000):
#     d = str(i)
#     if int(d[0]) % 2 == 0 and int(d[1]) % 2 == 0 and int(d[3]) % 2 == 0 and int(d[2]) % 2 == 0:
#         x = f(i)
#         if x == 414:
#             c+=1
# print(c)

#
# def F(n):
#     if n > 0:
#         F(n - 3)
#         print(n)
#         F(n // 3)
#
# print(F(9))

# def f(n, fin):
#     if n > fin:
#         return 0
#     if n == fin:
#         return 1
#     if n < fin:
#         return f(n+2, fin) + f(n*2, fin) + f(n+3, fin)
#
# print(f(2,11)* f(11, 22))


# def f(x):
#     a=0; b=1
#     while x > 0:
#         if x%2 > 0:
#             a += x%8
#         else:
#             b = b * (x%8)
#         x = x//8
#     return a, b
#
# for i in range(1000000000):
#     a, b = f(i)
#     if a == 2 and b == 12:
#         print (i)


