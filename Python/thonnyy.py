def rotate(text,n):
    index = n % len(text)
    first = text[:index]
    last = text[index:]
    return last + first
#print(rotate("1234"))
#print(rotate("ABCD"))

def isRotated(A,B):
    t = 1
    for i in range(len(A)):
        if rotate(A, t) == B:
            return True
        else:
            t += 1
    return False

#print(isRotated("ABCD","CDAB"))
#print(isRotated("ABCD","BCDA"))

a = 'I "ate" the "so-called" "snacks"'
b = '''"can't won't didn't"'''
c = '''"all's well that 
    ends on a new line"'''

print("========")
print(a)
print("========")
print(b)
print("========")
print(c)
print("========")
