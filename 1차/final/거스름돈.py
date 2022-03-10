# 14916
# https://www.acmicpc.net/problem/14916
n = int(input())

dp = [-1] * (n+1)
dp[0] = 0
for i in range(1, n+1):
    if i >= 2 and dp[i-2] > -1:
        if dp[i] == -1:
            dp[i] = dp[i-2]+1
        else:
            dp[i] = max(dp[i], dp[i-2]+1)
    if i >= 5 and dp[i-5] > -1:
        if dp[i] == -1:
            dp[i] = dp[i-5]+1
        else:
            dp[i] = max(dp[i], dp[i-5]+1)

print(dp[n])
