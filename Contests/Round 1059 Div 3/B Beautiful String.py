t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    
    pi = []
    

    for i in range(n):
        if s[i] == '0':
            pi.append(i + 1)
            
   
    print(len(pi))
   
    print(*pi)