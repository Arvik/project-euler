from prime import isPrime

def permuts(lc):
    "Generates all possible permutations of a given string"
    fl = lc[0]
    if len(lc) == 1 : 
        return [fl]
    pm = permuts(lc[1:])
    res = []
    for p in pm:
        res += [fl + p]
        res += [p + fl]
        for i in range(1, len(p)):
            res += [p[:i] + fl + p[i:]]
    return   res
    
if __name__ == '__main__':
    mxPr = 0
    base = "987654321"
    for i in range(len(base)):
        for s in permuts(base[i:]):
            y = int(s)
            if isPrime(y) and y > mxPr:
                mxPr = y
    print(mxPr)
