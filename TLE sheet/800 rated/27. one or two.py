
t = int(input())
 
for _ in range(t):
  n = int(input())
  
  arr = list(map(int,input().split()))
  
  a = arr.count(2)
  # print(a)
  
  if a == 0:
    print(1)
  
  elif a % 2 != 0:
    print(-1)
    
  else:
    
    half = a//2
    
    count = 0 
    
    for i in range(n):
      if arr[i] == 2:
        count += 1
        if count == half:
          print(i+1)
          break