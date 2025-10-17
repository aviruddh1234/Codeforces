t = int(input())
for _ in range(t):
    a, b, c, d = map(int, input().split())

  
    if d < b:
        print(-1)
        continue

  
    new_a = a + (d - b)

    
    if c > new_a:
        print(-1)
        continue
    
    
    total_moves = (d - b) + (new_a - c)
    print(total_moves)