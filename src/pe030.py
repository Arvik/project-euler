"""
The upper bound is ~ 6*9^5
"""
x = lambda n : sum([int(s)**5 for s in str(n) ])
l = [x(n) for n in range(2, 6*9**5) if x(n) == n] 
print(sum(l))

        
    
