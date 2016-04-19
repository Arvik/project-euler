amount = 200 

coins = (1, 2, 5, 10, 20, 50, 100, 200)

def memoize(f):
    results = {}  
    def lookup_f(*args):
        key = (args[0], args[1])
        res = results.get(key, None)        
        if res == None:
            res = f(*args)  # calculate the result for real
            results[key] = res  # and store it
        return res
    return lookup_f

def number_of_permutations(coins, amn=0):
    numop = 0
    for c in coins:
        left = amn - c
        if left > 0:
            numop += number_of_permutations(coins[coins.index(c):], left)
        elif left == 0:
            numop += 1
    return numop

number_of_permutations = memoize(number_of_permutations)
         
print(number_of_permutations(coins, amount)) # 73682         
