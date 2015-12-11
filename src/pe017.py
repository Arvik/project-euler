import re

dct = {0:"", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine",
        10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 15:"fifteen", 18:"eighteen",
        20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 80:"eighty", 1000:"one thousand"}

for k in range(1000):
    c, a, b = (k // 100) % 10, (k // 10) % 10, k % 10
    if k not in dct:
        r = ""
        if c >= 1:
            dct[k] = dct[c] + " hundred " + ("and" if (a + b > 0) else "") + dct[a * 10 + b]
        elif a == 1:
            dct[k] = r + dct[b] + "teen"
        elif b == 0:
            dct[k] = r + dct[a] + "ty"
        elif a > 1:
            dct[k] = r + dct[a * 10] + "-" + dct[b]
 
sm = 0
for k, w in dct.items():
    sm += len(re.sub(r"[-, ]", "", w))

print(sm)  # 21124
