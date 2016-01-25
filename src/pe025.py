a, b, count = 0, 1, 1
while b <= 10 ** 999: 
    a, b, count = b, a + b, count + 1
print(count)  # 4782
