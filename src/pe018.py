tr = (75, 95, 64, 17, 47, 82, 18, 35, 87, 10, 20, 4, 82, 47, 65, 19, 1, 23, 75, 3,
      34, 88, 2, 77, 73, 7, 63, 67, 99, 65, 4, 28, 6, 16, 70, 92, 41, 41, 26, 56,
      83, 40, 80, 70, 33, 41, 48, 72, 33, 47, 32, 37, 16, 94, 29, 53, 71, 44, 65, 25,
      43, 91, 52, 97, 51, 14, 70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57, 91, 71, 52, 38, 17, 14, 91, 43,
      58, 50, 27, 29, 48, 63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31, 4, 62, 98, 27, 23, 9, 70, 98, 
      73, 93, 38, 53, 60, 4, 23)

def smn(n):
    """The sum of the first n natural numbers"""
    return (n**2 + n) // 2

ln = len(tr) 
mxl = 0
while ln > 0:
    mxl+=1
    ln-=mxl 

mem = {} # memoization cache

def find_max(lvl = 0, pos = 0):
    z = mem.get((lvl,pos),None)
    if z is not None:
        return z
    sm = tr[smn(lvl)+pos]
    if lvl == mxl-1 :
        mem[(lvl,pos)] = sm 
        return sm
    sm_left = find_max(lvl+1,pos) # calculate sum of the left branch
    sm_right = find_max(lvl+1,pos+1) # calculate sum of the right branch
    sm += sm_left if sm_left > sm_right else sm_right
    mem[(lvl,pos)]=sm
    return sm

print(find_max(0,0))