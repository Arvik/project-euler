tr = []
with open('../data/p067_triangle.txt') as f:
    str = f.read().replace('\n',' ')
    tr = list(map(int, str[:-1].rsplit(' ')))

def smn(n):
    """The sum of the first n natural numbers"""
    return (n ** 2 + n) // 2

ln = len(tr) 
mxl = 0
while ln > 0:
    mxl += 1
    ln -= mxl 

mem = {}  # memoization cache

def find_max(lvl=0, pos=0):
    z = mem.get((lvl, pos), None)
    if z is not None:
        return z
    sm = tr[smn(lvl) + pos]
    if lvl == mxl - 1 :
        mem[(lvl, pos)] = sm 
        return sm
    sm_left = find_max(lvl + 1, pos)  # calculate sum of the left branch
    sm_right = find_max(lvl + 1, pos + 1)  # calculate sum of the right branch
    sm += sm_left if sm_left > sm_right else sm_right
    mem[(lvl, pos)] = sm
    return sm

print(find_max(0, 0))
