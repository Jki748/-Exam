print ("x y w z")

for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (not(w <= x) or (y <= z) or not(y)) == False:
                    print(x,y,w,z)
