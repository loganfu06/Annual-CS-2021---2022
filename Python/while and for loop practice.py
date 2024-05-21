def howManyDoub(n):
    s = 1
    d = 0
    while s < n:
        s = s * 2
        d = d + 1
    return d

#print(howManyDoub(24))

def sumDigits(n):
    i = n
    s = 0
    while i > 0:
        r = i % (10)
        i = i // (10)
        s = s + r
    return s

print(sumDigits(1000000003))