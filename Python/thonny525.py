f = open("names-1.txt")
csv = f.read()
f.close()

csvv = csv.strip().split("\n")
data = []
for line in csvv[1:]:
    data += [line.split(",")]

#Answer to 1
def mostPaid(L):
    best = 0.0
    name = ""
    for info in L:
        days = int(info[3]) - int(info[2])
        totalpay = float(info[1]) * float(days)
        if totalpay > best:
            best = totalpay
            name = info[0]
    print(name, best)

#mostPaid(data)

#Answer to 2
def leastDays(L):
    for info in L:
        days = int(info[3]) - int(info[2])
        L = [days] + L
    L.sort
    
        