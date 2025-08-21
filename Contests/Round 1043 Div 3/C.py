t = int(input())
for _ in range(t):
   n = int(input())
   x = 0
   ans = 0
   while n > 0:
       p = n % 3
       n //= 3
       if p > 0:
           val = 3**(x+1) + x * 3**(x-1)
           ans += p * val
       x += 1
   print(int(ans))