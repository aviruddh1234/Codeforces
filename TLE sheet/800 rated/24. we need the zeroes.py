t = int(input())
 
for _ in range(t):
  n = int(input())
  arr = list(map(int,input().split()))
  
  avi = 0 
  
  for i in arr:
    avi ^= i 
  
  
  if n%2 == 1:
    print(avi)
  
  else:
    if avi == 0:
      print(avi)
    
    else:
      print(-1)