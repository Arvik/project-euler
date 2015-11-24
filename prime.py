from math import sqrt

def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1) :
        if n % i == 0 : return False
    return True

def primeSeq() :
    for n in [2, 3]: yield n
    while True : 
        n += 2
        if (isPrime(n)) : yield n

def isPrimeFast(n):
    for i in range(int(sqrt(n)) + 1, 2) :
        if n % i == 0 :
            return False
    return True