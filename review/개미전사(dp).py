n = int(input())
ware = list(map(int, input().split()))
dp = [0] * 100

dp[0] = ware[0]
dp[1] = max(ware[0], ware[1])

for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2]+ware[i])

print(dp[n-1])
