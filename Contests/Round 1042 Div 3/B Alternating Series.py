t = int(input())
for _ in range(t):
    n = int(input())
    
    result = []
    
    for i in range(n):
        if i % 2 == 0:  
            result.append(-1)
        else:  
            result.append(3)
    
  
    if n % 2 == 0:
        result[-1] = 2
    
    print(*result)