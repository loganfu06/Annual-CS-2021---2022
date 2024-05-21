f = open("2012_SAT_Results50.csv", "r")
raw = f.read()
f.close()

raww = raw.strip().split("\n")
csv = []
for i in raww:
    csv += [i.split(",")]

for i in csv[1:]:
    i[2] = int(i[2])
    i[3] = int(i[3])
    i[4] = int(i[4])
    i[5] = int(i[5])

def mostTestTakers(L):
    sortedList = []
    for i in L[1:]:
        num = i[2]
        i = [num] + i
        sortedList += [i]
    sortedList.sort()
    for i in range(len(sortedList)):
        sortedList[i] = sortedList[i][1:]
    return sortedList[-1]
        
#print(mostTestTakers(csv))

def highestScore(L):
    sortedList = []
    for i in L[1:]:
        num = i[3] + i[4] + i[5]
        i = [num] + i
        sortedList += [i]
    sortedList.sort()
    for i in range(len(sortedList)):
        sortedList[i] = sortedList[i][1:]
    return sortedList[-1]\

#print(highestScore(csv))

def averages(L):
    totalRead = 0
    totalMath = 0
    totalWrite = 0
    for i in L[1:]:
        totalRead += i[3]
        totalMath += i[4]
        totalWrite += i[5]
    averageRead = totalRead / len(L[1:])
    averageMath = totalMath / len(L[1:])
    averageWrite = totalWrite / len(L[1:])
    return [averageRead] + [averageMath] + [averageWrite]

#print(averages(csv))


    

    