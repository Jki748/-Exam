# from itertools import product
# words = list(product("БЕРКЛИ","БЕРКЛИЙ","БЕРКЛИЙ","БЕРКЛИЙ"))
# k = 0
#
# for i in words:
#     w = ''.join(i)
#     if "Е" in w or "И" in w or 'Й' in w:
#         k +=1
#
# print(k)

from itertools import product

words = list(product("ГОЛ", repeat=20))
k = 0

for i in words:
    w = ''.join(i)
    if (i[0]=='Г' and i[19] == 'Г') or "ОГО" in w or 'ЛГЛ' in w:
        k += 1


print(len(words)-k)



