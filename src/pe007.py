"""
Problem 7:

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

from prime import primeSeq
from _datetime import datetime

start = datetime.now()
l = (p for i, p in enumerate(primeSeq()) if i == 10000)
print("Result:", next(l))
finish = datetime.now()

print("Elapsed time: ", finish - start)
