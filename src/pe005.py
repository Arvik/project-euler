"""
Problem 5:

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"
"""

def isDivisible(x, n=20):
    for i in range(2, n):
        if x % i != 0: return False
    return True

def genCandidates(base=20):
    cnt = 1
    while True:
        yield base * cnt
        cnt += 1

print(next((i for i in genCandidates() if isDivisible(i))))  # 232792560
