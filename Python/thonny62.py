
def MinMaxList(filename):
    f = open(filename,'r')
    nums = f.read()
    f.close()
    L = nums.strip().split("\n")
    wc = {}
    for w in L:
        x = wc.get(w,0)
        wc[w] = x + 1
    for i in range(len(L)):
        