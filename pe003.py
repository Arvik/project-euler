number= 600851475143

def isPrime(n):
    for i in range(2, n // 2 +1) :
        if n % i == 0 : return False
    return True

def primeSeq(count = 1) :
    n = 1
    cnt = 0
    while True : 
        n+=1
        if (isPrime(n)) : 
            yield n
            cnt +=1
        if (cnt >= count ) : return

def findPrimeMultipliers(n = 2):
    for m in primeSeq(100000) :
        while (n % m == 0 and int(n) != 1): 
            n = int(n / m)
            print(m," : ",n)
    
print(findPrimeMultipliers(number))