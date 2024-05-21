def sumAtoB(a,b):
    s = 0
    if a < b:
        for i in range(a, b + 1):
            s += i
            i += 1
        return s
    else:
        return("A must be less than B")
   
#print("sumAtoB(1,4) should be 10, and is: ", sumAtoB(1,4))
#print("sumAtoB(1,2) should be 3, and is: ", sumAtoB(1,2))
#print("sumAtoB(4,1) should be an error message, and is: ", sumAtoB(4,1))

def sumAuptoB(a,b):
    s = 0
    if a < b:
        for i in range (a,b):
            s += i
            i += 1
        return s
    else:
        return("A must be less than B")

#print("sumAuptoB(1,4) should be 6, and is: ", sumAuptoB(1,4))
#print("sumAuptoB(1,2) should be 1, and is: ", sumAuptoB(1,2))
#print("sumAuptoB(4,1) should be an error message, and is: ", sumAuptoB(4,1))

def sumFiveAuptoB(a,b):
    s = 0
    if a % 5 == 0 and a < b:
        for i in range (a,b):
            if i % 5 == 0:
                s += i
        return s
    else:
        return("A must be a multiple of 5 or A must be less than B")

#print("sumFiveAuptoB(5,20) should be 30, and is: ", sumFiveAuptoB(5,20))
#print("sumFiveAuptoB(0,20) should be 30, and is: ", sumFiveAuptoB(0,20))
#print("sumFiveAuptoB(5,25) should be 50, and is: ", sumFiveAuptoB(5,25))
#print("sumFiveAuptoB(5,0) should be an error message, and is: ", sumFiveAuptoB(5,0))
#print("sumFiveAuptoB(2,10) should be an error message, and is: ", sumFiveAuptoB(2,10))
    
def evaluateCubic(x):
    return x * (x - 2) * (x + 2)

#print("evaluateCubic(2) should be 0, and is: ",evaluateCubic(2))
#print("evaluateCubic(-2) should be 0, and is: ",evaluateCubic(-2))
#print("evaluateCubic(0) should be 0, and is: ",evaluateCubic(0))
#print("evaluateCubic(3) should be 15, and is: ",evaluateCubic(3))

def findMaxCubicAuptoB(a,b):
    greatest = evaluateCubic(a)
    if a < b:
        for i in range(a,b):
            if evaluateCubic(i) > greatest:
                greatest = evaluateCubic(i)
        return greatest
    else:
        return("A must be less than B")

#print("findMaxCubicAuptoB(-2,0) should be 3, and is: ", findMaxCubicAuptoB(-2,0))
#print("findMaxCubicAuptoB(0,2) should be 0, and is: ", findMaxCubicAuptoB(0,2))
#print("findMaxCubicAuptoB(-2,4) should be 15, and is: ", findMaxCubicAuptoB(-2,4))
#print("findMaxCubicAuptoB(3,0) should be an error message, and is: ", findMaxCubicAuptoB(3,0))

def fizzbuzz(n):
    if n > 1:
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                print("fizzbuzz")
            elif i % 3 == 0:
                print("fizz")
            elif i % 5 == 0:
                print("buzz")
            else:
                print(i)                
    else:
        print("N must be greater than 1")

#Test cases(I assumed n was inclusive)
#fizzbuzz(5)
#fizzbuzz(3)
#fizzbuzz(0)
#fizzbuzz(2)
