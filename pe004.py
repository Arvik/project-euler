
def isPalindrom(n):
    s = str(n)
    return s == s[::-1]

def findBiggest():
    return max([i * y for i in range(100, 999)for y in range (100, 999) if isPalindrom(i * y)]) 
                
if __name__ == '__main__':
    print(findBiggest())
