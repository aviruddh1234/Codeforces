t = int(input())

for _ in range(t):
  n,k = map(int,input().split())
  arr = list(map(int,input().split()))
  
  is_order = True 
  
  for i in range(1,n):
    if arr[i] < arr[i-1]:
      is_order = False 
  
  if is_order:
    print("YES")
  
  else:
    if k == 1:
      print("NO")
      
    else:
      print("YES")