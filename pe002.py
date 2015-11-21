def p2_fibonacci(n) :
    """
    Generates fibonacci sequence with a given number of elements
    """
    a,b = 1,2
    for _ in range(n) : 
        yield a
        a,b = b, a+b

def p2_lessthan(value=0) : 
    """"
    Returns a sum of fibonacci number which do not exceed given threshold
    """
    res = 0
    for i in p2_fibonacci(10000) : 
        if (i >= value) :
            break
        if i % 2 == 0 :
            res +=i;
    return res    

if __name__ == '__main__':
    print(p2_lessthan(4000000))
    
