from _datetime import datetime
from math import sqrt

started = datetime.now()

def get_all_divisors(n):
    res = [1]
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0 and n != i: 
            res += [i, n // i]
    return set(res)

def is_abudant(n):
    return sum(get_all_divisors(n)) > n
    
z = []
for i in range(1, 28123):  # 28123
    z += [i] if is_abudant(i) else []

n = []
for i in z:
    for j in z:
            n += [i + j]
n=set(n)

nn = [i for i in range(1, 28123) if i not in n]

print (sum(nn))  # 4179871
print (datetime.now() - started)                     
