n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))

count = 0
coin.sort(reverse=True)

for i in coin:
    count += k // i
    k = k % i

print(count)