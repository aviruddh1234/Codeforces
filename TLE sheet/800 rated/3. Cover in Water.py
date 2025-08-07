t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    avi = False
    for i in range(n - 2):
        if s[i] == '.' and s[i+1] == '.' and s[i+2] == '.':
            avi = True
            break
    
    if avi:
        print(2)
    else:
        empty_count = s.count('.')
        print(empty_count)