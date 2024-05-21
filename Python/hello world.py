def muricatemp(x):
    print(x * (9/5) + 32)
muricatemp(20)

def worldtemp(x):
    print((x - 32) * (5/9))
worldtemp(70)

a = 1
b = -4
c = 3

x = (-b + ((b**2 - 4 * a * c)**0.5)) / (2 * a)
x2 = (-b - ((b**2 - 4 * a * c)**0.5)) / (2 * a)

print(x, x2)
