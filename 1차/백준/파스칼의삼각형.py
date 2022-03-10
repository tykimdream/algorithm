n, k = map(int, input().split())

dp = [[] for i in range(n+1)]
dp[0].append(1)

for i in range(1, n+1):
    for j in range(i):
        if j == 0 or j == i-1:
            dp[i].append(1)
        else:
            dp[i].append(dp[i-1][j] + dp[i-1][j-1])
dp.pop(0)
# print(dp)
print(dp[n-1][k-1])
