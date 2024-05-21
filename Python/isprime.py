def isPrime(n):
    i = 2
    while i < n:
        if n % i == 0:
            return False
            break
        else:
            i += 1
    if i == n:
        return True
print(isPrime(17))