t = int(input())
for _ in range(t):
    n, k, x = map(int, input().split())
    
    if x != 1:
        print("YES")
        print(n)
        print(*[1] * n)
    else:
        if n == 1:
            print("NO")
        elif k == 1:
            print("NO")
        else:
            if n % 2 == 0:
                print("YES")
                print(n // 2)
                print(*[2] * (n // 2))
            else:
                if k >= 3:
                    print("YES")
                    print((n - 3) // 2 + 1)
                    result = [3] + [2] * ((n - 3) // 2)
                    print(*result)
                else:
                    print("NO")