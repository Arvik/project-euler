def gen_lexicogr_permutations(elements):
    lng = len(elements) 
    prmi = list(range(lng))
    yield [elements[i] for i in prmi]
    while (True):
        x = y = None
        for i in range(lng-1):
            x = i if prmi[i] < prmi[i+1] else x
        if x == None: return
        for i in range(lng):
            y = i if prmi[x] < prmi[i] else y
        prmi[x], prmi[y] = prmi[y],prmi[x]
        fprmi = prmi[:x+1] 
        lprmi = prmi[x+1:] 
        prmi = fprmi + lprmi[::-1]
        yield [elements[i] for i in prmi]
        
ps = gen_lexicogr_permutations(range(10))
print("".join(str(s) for s in next((p for i, p in enumerate(ps) if i == 1000000)))) #2783915604
