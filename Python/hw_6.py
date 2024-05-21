def countLetter(text, letter):
    s = 0
    for i in range(len(text)):
        if text[i] == letter:
            s += 1
    return s

#print(countLetter("trees", "t"))
#print(countLetter("trees", "e"))

def findLetter(A, B):
    for i in range(len(A)):
        if A[i] == B:
            return i
    return -1

#print(findLetter("fish","f"))
#print(findLetter("fish","F"))
#print(findLetter("lool","l"))

def emphasize(text):
    s = ""
    for i in range(len(text)):
        if text[i] == ".":
            s += "!"
        else:
            s += text[i]
    return s

#print(emphasize("Hi. You're great."))
#print(emphasize("HI........ BYE."))

def isVowel(c):
    if c == "A" or c == "a" or c == "E" or c == "e" or c == "I" or c == "i" or c == "O" or c == "o" or c == "U" or c == "u" or c == "Y" or c == "y":
        return True
    else:
        return False

#print(isVowel("A"))
#print(isVowel("B"))

def countVowels(A):
    s = 0
    for i in range(len(A)):
        if isVowel(A[i]) == True:
            s += 1
    return s

#print(countVowels("aAbeE"))
#print(countVowels("adbausjhduaniuwyasan"))

def justTheVowels(A):
    s = ""
    for i in range(len(A)):
        if isVowel(A[i]) == True:
            s += A[i]
    return s

#print(justTheVowels("Aw, seriously??"))
#print(justTheVowels("Bzzt chhhggk"))

def everyOther(A, startAt):
    s = ""
    for i in range(len(A)):
        if A[startAt] % 2 == 0:
            s += A[i]
    return s

print(everyOther("a1b2c3",0))