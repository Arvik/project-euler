
def isPalindromic(n):
    cl = list(str(n))
    rcl = cl[::-1]
    for i in range(len(cl)) :
        if cl[i] != rcl[i]: 
            return False
    return True

def findBiggest():
    maxRes = 0;
    for i in range(100,1000):
        for y in range (100, 1000):
            candidate = i*y
            if isPalindromic(candidate) and candidate > maxRes: maxRes = candidate
    return max 
                

if __name__ == '__main__':
    print(findBiggest())