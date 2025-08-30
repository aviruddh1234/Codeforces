def gcd(a,b):
  if a == 0:
    return b 
  else:
    return gcd(b%a,a)
    
t = int(input())
for _ in range(t):
  n = int(input())
  arr = list(map(int,input().split()))
  
  flag = True 
  
  for i in range(n):
    for j in range(i+1,n):
      a = max(arr[i],arr[j])
      b = min(arr[i],arr[j])
      
      if gcd(a,b) > 2:
        flag = False 
        break
    
  
  if flag:
    print("Yes")
  else:
    print("No")
      