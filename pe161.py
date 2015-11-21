from _datetime import datetime

figures = {
           0:[ [1, 1, 0],
                 [1, 0, 0],
                 [0, 0, 0]],
           1:[ [1, 1, 0],
                 [0, 1, 0],
                 [0, 0, 0]],
           2:[ [1, 0, 0],
                 [1, 1, 0],
                 [0, 0, 0]],
           3:[ [0, 1, 0],
                 [1, 1, 0],
                 [0, 0, 0]],
           4:[ [1, 0, 0],
                 [1, 0, 0],
                 [1, 0, 0]],
           5:[ [1, 1, 1],
                 [0, 0, 0],
                 [0, 0, 0]],
           }

#mx = 2
#my = 9
mx = 9
my = 12

msize = mx * my

def memoize(f):
    results = {}  
    def lookup_f(*args):
        key = (args[0], args[2])
        res = results.get(key, None)        
        if res == None:
            res = f(*args)  # calculate the result for real
            results[key] = res  # and store it
        return res
    return lookup_f

def flatten_mtx(mtx, x=None, y=None):
    "Flattens two-dimensional array 0..x,0..y"
    x = x if x else len(mtx)
    y = y if y else len(mtx[0])
    res = [e for sublist in mtx[:x] for e in sublist[:y]]
    rn = 0
    for i, r in enumerate(res):
        rr = r << i
        rn = rn | rr
    return rn 


def check_matrix(mtx):
    for x in range(len(mtx)):
        for y in range(len(mtx[0])):
            if mtx[x][y] == 1 and (x >= mx or y >= my) :
                return False 
    return True

def gen_positions():
    ppos = {}
    idx = 0
    for figure in figures:
        for x in range(mx):
            for y in range(my):
                pos = [[0 for _ in range(my + 2)] for _ in range(mx + 2)]
                for ax in range(3):
                    for ay in range(3):
                        vl = figures[figure][ax][ay]
                        pos[x + ax][y + ay] += vl
                if (check_matrix(pos)) :
                    ppos[idx] = flatten_mtx(pos, mx, my) 
                    (x for x in pos)
                    idx += 1
    return ppos

def build_dot_map(dpos):
    "Computes a dictionary where kyes are equal to a index within a flatten array and values correspond to positions which has non-zero value at this index "
    dmap = { p : [] for p in range(msize) }
    for k in dpos:
        pos = dpos[k]
        for i in range(msize - 1):
            bit = (pos >> i) & 1;
            if bit == 1 : 
                dmap[i] += [pos]
    return dmap

dpositions = gen_positions()
dot_map = build_dot_map(dpositions)

total = 0
total_found = 0

started = datetime.now()

def find(d_from, d_to, trace):
    global total, total_found
    total += 1
    # print("total = ",total," dfrom=",d_from, "trace=",'{0:08b}'.format(trace)[::-1])
    t = 0
    if trace == 0:
        dc = dot_map[d_from];
        for d in dc: 
            t += find(d_from, d_to, trace | d)
        return t
    
    # find last_dot in trace
    last_dot = d_from
    
    for i in range(d_from, d_to - 1):
        bit1 = (trace >> i) & 1;
        bit1p1 = (trace >> (i + 1)) & 1;
        if bit1 == bit1p1 == 1 :
            last_dot = i + 1
        else:
            break
    
    if last_dot == d_to - 1:
        total_found += 1
        return 1

    for c in dot_map[last_dot + 1]:
        if trace & c == 0 : #check for overlap
            t += find(last_dot+1, d_to, trace | c)  
    return t

find = memoize(find)  # enable memoization 

print("Starting at ", started)
s = find(0, mx * my - 1, 0)
finish = datetime.now()
print("Elapsed time:", finish - started)
print("Total invocations: ", total)
print("Total solution_found's: ", total_found)
print("\nResult = ", s)
