from collections import Counter 
t = int(input())

for _ in range(t):
  n = int(input())
  arr = list(map(int,input().split()))
  
  count = Counter(arr)
  
  flag = False 
  
  for i, n in count.items():
    if n >= 2:
      flag = True
      break 
  
  if flag:
    print("YES")
  else:
    print("NO")
  
  
  