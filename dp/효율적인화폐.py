n, m = map(int, input().split())

coin = list(map(int, input().split()))
d = [10001] * (m+1)

d[0] = 0

for i in range(n):
    for j in range(coin[i], m+1):
        if d[j-coin[i]] != 10001:
            d[j] = min(d[j], coin[i]+1)

print(d[m])
