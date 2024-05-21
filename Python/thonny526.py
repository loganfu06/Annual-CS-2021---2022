f = open("name_and_wage_first10.txt", "r")
csv = f.read()
f.close()
stringData = csv.strip().split("\n")[1:]
data = []
for i in stringData:
    