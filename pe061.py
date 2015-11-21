
def figural_number(ft, n):
    op = { 
                3: lambda x: x * (x + 1) // 2,
                4: lambda x: x * x,
                5: lambda x: x * (3 * x - 1) // 2,
                6: lambda x: x * (2 * x - 1),
                7: lambda x: x * (5 * x - 3) // 2,
                8: lambda x: x * (3 * x - 2)
           }
    return op[ft](n) 

def find_num(dct, startWith):
    "Finds numbers in a dictionary which start with a given string."
    res = {}
    strStartsWith = str(startWith)
    for e in dct:
        res[e] = []
        for n in dct[e]:
            if str(n)[:2] == strStartsWith : res[e] += [n] 
    return res

def copy_dict_without_key(dct, k=None):
    res = dct.copy()
    res.pop(k, None)
    return res

def find_seq(k, num, nms_dct) :
    "Finds number sequence"
    res = []
    r_nums = copy_dict_without_key(nms_dct, k) 
    nextnn = find_num(r_nums, str(num)[2:])
    nextnn = {k: v for k, v in nextnn.items() if len(v) > 0}  # filters empty lists
    if len(nextnn) == 0 :
        return [[num]]
    else:
        for k, v in nextnn.items():
            rr_nums = copy_dict_without_key(r_nums, k)
            for tail in find_seq(k, v[0], rr_nums):
                seq = [num]+tail
                res.append(seq)
    return res

def gen_dictionary(): 
    "Compute dictionary of 4 digits figural numbers"
    nums = {}
    for fig_type in range(3, 9):
        nums[fig_type] = []
        last_num = 0
        cnt = 1;
        while last_num < 10000:
            last_num = figural_number(fig_type, cnt)
            if 10000 > last_num > 999: nums[fig_type] += [last_num]
            cnt += 1
    return nums

ndict = gen_dictionary()
found = None
for k in ndict:
    for v in ndict[k]:
        sqs = find_seq(k, v, ndict)
        for sq in sqs :
            if len(sq) == 6 and str(sq[0])[:2] == str(sq[-1])[2:]:
                found = sq
    if found :
        print("Found: %s, sum = %d" % (found,sum(found)))
        break

                
            
            
        
        
        
