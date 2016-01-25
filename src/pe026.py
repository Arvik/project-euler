"""
Find the value of d < 1000 for which 1/d contains the longest 
recurring cycle in its decimal fraction part.
"""
def lenCycle(i, n): 
    rst = []
    while i != 0:
        d = i * 10 // n
        i = i * 10 - d * n
        if (i in rst):
            return len(rst)
        rst += [i]
    return 0

cl = [lenCycle(1,x) for x in range (1,1000)]
print (cl.index(max(cl))+1) # 983



