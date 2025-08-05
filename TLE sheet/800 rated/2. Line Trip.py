t = int(input())
for _ in range(t):
  
  n,x = map(int,input().split())
  arr = list(map(int,input().split()))
  
  maxx = 0 
  maxx = max(maxx,arr[0])
  
  
  for i in range(n-1):
    curr = arr[i+1]- arr[i]
    maxx = max(maxx, curr)
  
  a = (x - arr[-1])*2
  maxx = max(maxx,a)
  
  print(maxx)