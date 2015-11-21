
def isPrime(n):
    for i in range(2, n // 2+1) :
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
        
if __name__ == '__main__':
        print(list(primeSeq(10001))[-1])
    