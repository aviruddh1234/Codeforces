t = int(input())
for _ in range(t):
  n = int(input())
  arr = list(map(int,input().split()))
  
  res = []
  
  res.append(arr[0])
  
  for i in range(1, n):
    
    if arr[i] < arr[i-1]:
      if (arr[i] == 1):
        res.append(1)
       
      else: 
        res.append(arr[i]-1)
      
      res.append(arr[i])
      
    else:
      res.append(arr[i])
  
  print(len(res))
  
  print(*res)