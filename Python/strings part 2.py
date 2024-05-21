def countSentences(string):
    sentences = 0
    for i in range(len(string)):
        if string[i] == ".":
            sentences += 1
    return sentences

print(countSentences("Hello. smasdnahduiwhuihadwiua. daw7hdiusahdiuhsauid."))

def checkDNA(dna1, dna2):
    checkthis = ""
    for i in range(len(dna1)):
        if dna1[i] == "A":
            checkthis = checkthis + "T"
        elif dna1[i] == "T":
            checkthis += "A"
        elif dna1[i] == "C":
            checkthis += "G"
        elif dna1[i] == "G":
            checkthis += "C"
    if checkthis == dna2:
        return True
    else:
        return False
    
print(checkDNA("AAGATC", "TTCTAG"))
            