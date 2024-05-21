def orderInAlphabet(char):
    up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    low = "abcdefghijklmnopqrstuvwxyz"
    for i in range(0,len(up),1):
        if up[i] == char:
            return i
        if low[i] == char:
            return i
    return -1

#print(orderInAlphabet("A"))

def charToUpperCase(char):
    i = orderInAlphabet(char)
    if i == -1:
        return char
    else:
        return up[i]
    
print(ord("A"))
print(ord("0"))
print(ord("/"))
print(ord(" "))
print(chr(32))
print(chr(29999))
print(chr(10084))
print(chr(69420))