number= 600851475143

def isPrime(n):
    for i in range(2, n // 2 +1) :
        if n % i == 0 : return False
    return True

def primeSeq() :
    for n in [2,3]: yield n
    while True : 
        n+=2
        if (isPrime(n)) : yield n

def findPrimeMultipliers(n = 2):
    res = 1
    for m in primeSeq():
        while (n % m == 0 and n != 1): 
            n = n / m
            res = m
        if n == 1 : break
    return res
    
print(findPrimeMultipliers(number))