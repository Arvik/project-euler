
def isPrime(n):
    for i in range(2, n // 2 +1) :
        if n % i == 0 : return False
    return True

def primeSeq() :
    for n in [2,3]: yield n
    while True : 
        n+=2
        if (isPrime(n)) : yield n