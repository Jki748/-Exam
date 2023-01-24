# # (5x + 3y ≠ 60) ∨ ((A > x) ∧ (A > y))
#
# for A in range(300):
#     k = 0
#     for x in range(300):
#         for y in range(300):
#             if (5*x + 3*y != 60) or ((A > x) and (A > y)):
#                 k +=1
#
#     if k == 90000:
#         print(A)


# x&17 = 0 → (x&29 ≠ 0 → x&А ≠ 0)


# for A in range(300):
#     k = 0
#     for x in range(300):
#         if (x&17 == 0) <= ((x&29 != 0) <= (x&A != 0)):
#             k +=1
#
#     if k == 300:
#         print(A)


# (y + 2x ≠ 48) ∨ (A < x) ∨ (x < y)


# for A in range(300):
#     k = 0
#     for x in range(300):
#         for y in range(300):
#             if (y + 2*x != 48) or (A < x) or (x < y):
#                 k +=1
#
#     if k == 90000:
#         print(A)



# x&51 = 0 ∨ (x&41 = 0 → x&А = 0)

#
# for A in range(300):
#     k = 0
#     for x in range(300):
#         if (x&51 == 0) or ((x&41 == 0) <= (x&A == 0)):
#             k +=1
#
#     if k == 300:
#         print(A)








# x&25 ≠ 0 → (x&17 = 0 → x&А ≠ 0)

for A in range(300):
    k = True
    for x in range(300):
        if ((x&25 != 0) <= ((x&17 == 0) <= (x&A != 0))) == 0:
            k = False
    if k:
        print(A)


# for A in range(32):
#     B = True
#     for x in range(32):
#         if ((x&25==0) or (x&17!=0) or (x&A!=0))==0:
#             B=False
#     if B:
#         print(A)
#         break





