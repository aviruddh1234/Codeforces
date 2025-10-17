
t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    if a == b:
        print(0)
  
    elif a.bit_length() < b.bit_length():
        print(-1)
        
    
    else:
      x = a^b
      
      if x <= a:
        print(1)
        print(x)

      else:
          print(2)
          print(b, a)

