from math import sqrt

def get_all_divisors(n):
    res = [1]
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0 : 
            res += [i, n // i]
    return res

ds = {}
for i in range(1, 10001):
    ds[i] = sum(get_all_divisors(i))

amicable_numbers = [k for k, v in ds.items() if ds[k] != k and ds[k] in ds and k == ds[v]]

print(sum(amicable_numbers))  # 31626     
