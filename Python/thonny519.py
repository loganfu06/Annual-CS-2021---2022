def average(L):
    sum = 0
    for i in range(len(L)):
        sum += L[i]
    return sum / len(L)

def median(L):
    if len(L) / 2 == 0:
        return (L[int(len(L) / 2) - 1] + L[int(len(L) / 2)]) / 2
    else:
        return L[int(len(L) / 2)]

print(median([1,2,3,3]))
