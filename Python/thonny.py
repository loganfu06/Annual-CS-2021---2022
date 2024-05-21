def rCRC(t):
    text = ""
    previous = ""
    for i in range(len(t)):
        if previous == t[i]:
            continue
        else:
            text += t[i]
        previous = t[i]
    return text

#print(rCRC("bruuuuuuuuuuuuuuuhhhhhhhhhhhhh"))

def lastFirst(fullname):
    name = ""
    space = False
    for i in range(len(fullname)):
        if space == True:
            name += fullname[i]
        elif fullname[i] == " ":
            space = True
    name += ", "
    for i in range(len(fullname)):
        if fullname[i] == " ":
            break
        else:
            name += fullname[i]
    return name

#print(lastFirst("Joe Mama"))

digraphs = ['bl', 'br', 'ch', 'ck', 'cl', 'cr', 'dr', 'fl', 'fr', 'gh', 'gl', 'gr', 'ng', 'ph', 'pl', 'pr', 'qu', 'sc', 'sh', 'sk', 'sl', 'sm', 'sn', 'sp', 'st', 'sw', 'th', 'tr', 'tw', 'wh', 'wr']

print('bl' == digraph)