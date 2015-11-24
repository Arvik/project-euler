"""

a^x > b^y
log(a^x) > log(b^y)
x*log(a) > y(log(b)

"""

import math

mtx = []
f = open('problems/p099_base_exp.txt')
mtx = [list(map(int, line[:-1].rsplit(','))) for line in f]
rs = [m[1]*math.log(m[0]) for m in mtx]
print(rs.index(max(rs)))
    
    