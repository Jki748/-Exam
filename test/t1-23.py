def f(s, fin):
    if s > fin:
        return 0
    if s == fin:
        return 1
    if s == 17:
        return 0
    if s < fin:
        return f(s+1, fin) + f(s*2, fin) + f(s**2, fin)

print(f(2,16)*f(16,65))