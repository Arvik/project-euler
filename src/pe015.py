"Problem #15. This solution is an adaptation of solution to #81"

w = h = 21 # 20x20 grid corresponds to 21x21 matrix

mtx = []
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
        return 1
    rr = dd = 0
    if x < w - 1:
        rr += find(x + 1, y)
    if y < h - 1:
        dd += find(x, y + 1)
    return rr+dd

find = memoize(find)

print(find(0, 0))
    
        
