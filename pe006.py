
nn = range(101) # 1..100
"nns = [x*x for x in nn]"
nns = map (lambda x: x*x,nn)
print(sum(nn)**2 - sum(nns))