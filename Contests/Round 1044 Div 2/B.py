t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    
    total = 0
    for i in range(n-1, -1, -2):
        total += arr[i]
    
    print(total)