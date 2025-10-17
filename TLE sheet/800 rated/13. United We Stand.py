
t = int(input())
 
for _ in range(t):
  n = int(input())
  arr = list(map(int,input().split()))
  b = []
  c = []
  
  avi = min(arr)
  
  for i in arr:
    if i == avi:
      b.append(i)
    
    else:
      c.append(i)
  
  if len(b) == 0 or len(c) == 0:
    print(-1)
  
  else:
    print(len(b),end=" ")
    print(len(c))
    
    print(*b)
    print(*c)