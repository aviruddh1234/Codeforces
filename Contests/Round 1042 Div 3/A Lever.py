t = int(input())
for _ in range(t):
  n = int(input())
  a = list(map(int,input().split()))
  b = list(map(int,input().split()))
  res = 0 
  
  for i in range(n):
    if a[i] > b[i]:
      res += a[i]-b[i]
  
  res+= 1 
  print(res)