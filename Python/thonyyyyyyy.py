def pigLatin(word):
    first = ""
    last = ""
    currentIndex = 0
    vowels = ['a','e','i','o','u']
    digraphs = ['bl', 'br', 'ch', 'ck', 'cl', 'cr', 'dr', 'fl', 'fr', 'gh', 'gl', 'gr', 'ng', 'ph', 'pl', 'pr', 'qu', 'sc', 'sh', 'sk', 'sl', 'sm', 'sn', 'sp', 'st', 'sw', 'th', 'tr', 'tw', 'wh', 'wr']
    while currentIndex < len(word):
        if word[currentIndex:currentIndex+2] in digraphs:
            last += word[currentIndex:currentIndex+1]
            currentIndex += 2
        else:
            first += word[currentIndex]
            currentIndex += 1
    if word[0] in vowels
        return first + last + 'hay'
    else:
        return first + last

print(pigLatin("the"))