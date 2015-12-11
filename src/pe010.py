from prime import primeSeq

#142913828922
ps = 0
for p in primeSeq():
    if p >= 2000000: break
    ps += p
print(ps)
