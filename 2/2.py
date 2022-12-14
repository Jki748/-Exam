# (x → y) ∧ (¬x → ¬z) ∨ w

def f(x, y, w, z):
   return ((x <= y) and ((not x) <= (not z)) or w)

p = [0,1]
print('x y w z')
for x in p:
   for y in p:
       for w in p:
           for z in p:
               if not f(x, y, w, z):
                   print(x, y, w, z)