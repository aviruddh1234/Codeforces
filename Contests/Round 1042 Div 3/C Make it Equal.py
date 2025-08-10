from collections import defaultdict
 
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    c1 = defaultdict(int)
    c2 = defaultdict(int)
    
    for i in a:
        r = i % k
        q = (k - r) % k
        if r > q:
            r, q = q, r
        c1[(r, q)] += 1
    
    for i in b:
        r = i % k
        q = (k - r) % k
        if r > q:
            r, q = q, r
        c2[(r, q)] += 1
    
    print("YES" if c1 == c2 else "NO")