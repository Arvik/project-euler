"""
Problem 6
The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)**2 = 55**2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

nn = range(101)
nns = map (lambda x: x * x, nn)
print(sum(nn) ** 2 - sum(nns))

"""
This problem can also be solved using the following formulas:

i) Sum of first n numbers = n(n+1)/2
ii) Sum of squares of first n numbers = n(n+1)(2n+1)/6
"""

