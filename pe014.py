
ref = {}
def find(num):
    ref_r = ref.get(num, None) 
    if ref_r is not None:
        return ref_r
    num = num // 2 if num % 2 == 0 else 3 * num + 1  
    r = 1
    if num != 1: 
        r += find(num)
    ref[num]=r
    return r
    
mi, mx = 0, 0
for i in range(1, 999999):
    r = find(i)
    if r > mx: mi, mx = i, r

print(mi)
