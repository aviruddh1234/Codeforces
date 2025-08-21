t = int(input())
for _ in range(t):
    n = int(input())
    
    a = 10
    res = []
    
    while a < n:
        if n % (a + 1) == 0:
            res.append(n // (a + 1))
        a *= 10
    
    print(len(res))
    if res:
        res.reverse()
        print(*res)