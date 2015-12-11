import math

for a in range(1,1000):
    for b in range(1,1000):
        c = int(math.sqrt( a**2+b**2)) 
        if c**2 == a**2+b**2 and a+b+c==1000 and a<b<c:
            print(a*b*c)
        