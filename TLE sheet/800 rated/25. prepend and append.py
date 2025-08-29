t = int(input())
 
for _ in range(t):
  n = int(input())
  s = input()
  
  res = n 
  left = 0 
  right = n-1 
  
  while left <= right:
    if (s[left] != s[right]):
      res -= 2 
    
    else:
      break 
    
    left += 1 
    right -= 1 
  
  print(res)