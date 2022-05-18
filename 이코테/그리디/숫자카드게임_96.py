n, m = map(int, input().split())

result = 1

for _ in range(n):
    data = list(map(int, input().split()))
    temp = min(data)
    result = max(result, temp)

print(result)
