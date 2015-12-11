feb = lambda y : 1 if y % 4 == 0 and y % 400 != 0 else 0 
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mmm = [months[m] + (feb(y) if m == 1 else 0) for y in range(1901, 2001) for m in range(12)]

day_of_week = 0
res = 0
for m in mmm[:-1]:
    day_of_week = (day_of_week + m) % 7
    if day_of_week == 0:
        res+=1
print(res)