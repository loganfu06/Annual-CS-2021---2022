def overlap(n,times):
    s = 0
    r = times
    while r > 0:
        s = s + n * (10 ** r)
        r = r - 1
    return int(s / 10)

print(overlap(111,2))

#Challenges
def firstNPerfect(n):
    for i in range(0,n):
        ss = 0
        s = 0
        p = 1
        if i % p = 0:
            s = s + p
            ss = s + ss
            p = p + 1
            
            