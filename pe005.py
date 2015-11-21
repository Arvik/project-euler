
def isDivisible(x, n=20):
    for i in range(2,n):
        if x % i != 0: return False
    return True

def genCandidates(base = 20):
    cnt = 1
    while True:
        yield base * cnt
        cnt +=1

def find():
    lg = genCandidates()
    for i in lg:
        if isDivisible(i): 
            print(i)
            return i
    
print(find())