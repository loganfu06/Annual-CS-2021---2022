def add1Mutate(L):
    for i in L:
        L[i] += 1
    return L

def add1Copy(L):
    new = []
    for i in L:
        