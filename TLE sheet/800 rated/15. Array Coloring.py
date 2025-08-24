t = int(input())

for _ in range(t):
  n = int(input())
  arr = list(map(int,input().split()))
  
  count = 0 
  for i in arr:
    if i %2 !=0:
      count += 1 
  
  if count %2 == 0:
    print("YES")
  
  else:
    print("NO")
  
  