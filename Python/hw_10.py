def shiftOne(someText):
    s = ""
    for i in range(len(someText)):
        if someText[i] == "Z":
            s += "A"
        else:
            s += chr(ord(someText[i]) + 1)
    return s

#print(shiftOne("BZDRZQ"))
#print(shiftOne("HAL"))

def shiftN(someText, n):
    s = ""
    for i in range(len(someText)):
        if ord(someText[i]) + n > ord("Z"):
            diff = (ord(someText[i]) + n) - ord("Z")
            s += chr(64 + diff)
        else:
            s += chr(ord(someText[i]) + n)
    return s

#print(shiftN("ABC", 25))
#print(shiftN("ABC", 26))
#print(shiftN("KZNEXFGURFCBG", 13))
            