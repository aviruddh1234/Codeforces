n = int(input())
arr = list(map(int,input().split()))

res = []

for i in arr:
    res.append(abs(i))

print(min(res))