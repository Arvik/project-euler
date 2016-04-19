levels = 1001

x,sum = 1,1
for i in range(2,1001, 2) :
    for ii in range(4):
        x+=i
        sum += x 
print(sum)