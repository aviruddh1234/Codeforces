t = int(input())

for _ in range(t):
  n = int(input())
  
  count = len(list(str(n)))
  first = int(list(str(n))[0])
  
  print(9*(count-1)+first)
  
  