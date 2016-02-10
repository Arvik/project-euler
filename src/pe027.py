from math import sqrt

def isPrime(n):
    if n < 0: return False
    for i in range(2, int(sqrt(n)) + 1) :
        if n % i == 0 : return False
    return True

n, mi, my = 0, 0, 0

def calculate(nn, a, b):
    return nn * nn + nn * a + b

for i in range(-1000, 1000):
    for y in range (-1000, 1000):
        # start with the longer sequence already found + 1 
        nn = n + 1
        while isPrime(calculate(nn, i, y)): 
            nn += 1
        if (nn > n + 1):
            failed = False
            # check new candidate 
            for z in range(0, nn):
                if not isPrime(calculate(z, i, y)): 
                    failed = True
                    break
            if not failed: 
                n, mi, my = nn, i, y
print("Result: sequence length = %s, a=%s, b=%s, product=%d" % (n, mi, my, mi * my))
        
            
        
