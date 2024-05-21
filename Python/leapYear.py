def is_leap(n):
    if n % 4 == 0:
        if n % 400 == 0 and n % 100 == 0:
            return True
        if n % 100 == 0:
            return False
        else:
            return True
    else:
        return False
            
print("is_leap(2001) should be False, is:", is_leap(2001))
print("is_leap(2020) should be True, is:", is_leap(2020))
print(is_leap(1900))
