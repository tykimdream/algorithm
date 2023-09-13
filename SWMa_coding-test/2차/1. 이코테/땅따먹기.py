land = [[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]

dp = [0] * 4
dp[0] = max(land[0])
dp[1] = max(dp[0], max(land[1]))
temp = max(land[1])
dp[2] = max(dp[0]+temp, dp[1])

print(dp[2])
# n = len(land)

# for i in range(2, n+1):
#     temp = max(land[i])
#     dp[i] = max(dp[i-2]+temp, dp[i-1])

# answer = dp[n-1]

# print(answer, dp)
