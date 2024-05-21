def mySum(L):
    sum = 0
    for i in range(len(L)):
        sum += L[i]
    return sum
#print(mySum([1,2,3]))

def myRange(n):
    L = []
    for i in range(n):
        L += [i]
    return L

#print(myRange(3))