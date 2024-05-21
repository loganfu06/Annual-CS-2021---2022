def addOne(x):
    return x + 1

def quadratFormPlusRoot(a, b, c):
    return (-b + ((b**2 - 4 * a * c)**0.5)) / (2 * a)

print(quadratFormPlusRoot(1, -4, 3))
print(quadratFormPlusRoot(1, 0, -1))

def lastdigit(x):
   return x % 10

print(lastdigit(324324324532432421))