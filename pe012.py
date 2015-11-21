from math import sqrt

def triangle_number(n):
    return sum(range(n+1))

def count_divisors(n):
    cnt=1
    sqn = int(sqrt(n))
    for i in range (1,sqn):
        if n % i == 0 : cnt+=2
    if sqn**2 == n : cnt-=1
    return cnt

divs = 0
trn = 2
while divs < 500 : 
    tr=triangle_number(trn)
    trn+=1
    divs = count_divisors(tr)
    print(tr, ':',divs)
    