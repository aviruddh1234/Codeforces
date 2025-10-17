t = int(input())
for _ in range(t):
  n = int(input())
  
  nums = list(map(int,input().split()))
  
  res = 0 
  
  for i in range(n):
    if nums[i] == 1:
      continue
    
    else:
      l = i 
      r = i
      
      while r < n and nums[r] == 0:
        r += 1 
      
      res = max(res,r-l)
  
  print(res)
      