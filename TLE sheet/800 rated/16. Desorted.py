def is_sorted(arr):
    for i in range(1,len(arr)):
      if arr[i-1] > arr[i]:
        return False
    
    return True

t = int(input())

for _ in range(t):
  n = int(input())
  arr = list(map(int,input().split()))
  
  if is_sorted(arr):
    res = float('inf') 
    for i in range(1, n):
      a = (arr[i] - arr[i-1])//2+1
      res = min(res,a)
    
    print(res)
  else:
    print(0)
  
  
  
  
  
  