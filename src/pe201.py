from _datetime import datetime

k = 50
n = 100

started = datetime.now()

arr = list(i ** 2 for i in range(1, n + 1))

mx = sum(arr[n - k:])                               # maximum total sum

dp = [[0 for _ in range(mx+1)] for _ in range(k+1)] 
dp[0][0] = 1 

for ai in arr:                                      # values in the sequence 1**2, 2**2...
    for j in range(k, 0, -1):                       # positions from k..0
        for kk in range(mx, ai - 1, -1):            # from maximum sum to ai-1 
                dp[j][kk] += dp[j - 1][kk - ai]      
                
res = 0
for z in range(mx+1):
    res += z if dp[k][z] == 1 else 0 

print(res)                                          # correct answer = 115039000

print(datetime.now() - started)                     # ~10 minutes using python and below 1 minute with Java