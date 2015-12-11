"""
Problem 4:

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def isPalindrom(n):
    s = str(n)
    return s == s[::-1]

def findBiggest():
    return max([i * y for i in range(100, 999) for y in range (100, 999) if isPalindrom(i * y)]) 
                
if __name__ == '__main__':
    print(findBiggest())
