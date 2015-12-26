names = []
with open('../data/p022_names.txt') as f:
     names = eval('['+ f.read()+']')
names.sort()
s = 0
for i,n in enumerate(names):
    s+= (i+1)*(sum([ord(c) - ord('A') + 1 for c in n]))
print(s) # 871198282