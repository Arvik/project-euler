levels = 999 # 1001 -3

x = 1
sum = x
for i in range(2,levels+3, 2) :
    for ii in range(4):
        x+=i
        sum += x 
print(sum)