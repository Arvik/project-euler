max_a = 100
max_b = 100

print(len(set(i ** j for i in range(2, max_a + 1) for j in range(2, max_b + 1))))
