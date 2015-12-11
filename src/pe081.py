"""
Problem 81:

Find the minimal path sum, in p081_matrix.txt file from the top left to the bottom right by only moving right and down.
"""
w = h = 80

mtx = []
f = open('../data/p081_matrix.txt')
mtx = [list(map(int, line[:-1].rsplit(','))) for line in f]

def memoize(f):
    res={}
    def lookup_f(*args):
        rt = res.get(args,None)
        if rt == None:
            rt = f(*args)
            res[args]=rt
        return rt
    return lookup_f
    
def find(x, y):
    if x == w - 1 and y == h - 1:
        return mtx[x][y]
    rr = dd = 2**30
    if x < w - 1:
        rr = find(x + 1, y)
    if y < h - 1:
        dd = find(x, y + 1)
    return mtx[x][y] + min([rr, dd])

find = memoize(find)

print(find(0, 0))
    
        
