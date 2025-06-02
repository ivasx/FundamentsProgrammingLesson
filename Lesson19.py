a = 2
b = 9
c = -4

res = a if a >= b else b

m = (a if a < c else c) if a < b else (b if b < c else c)
print(m)