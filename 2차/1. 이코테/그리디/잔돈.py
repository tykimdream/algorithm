n = int(input())

coins = [500, 100, 50, 10]
result = 0

for i in coins:
    result += n // i
    n %= i

print(result)
