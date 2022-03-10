# n = int(input())

# dp = [1, 1]

# for i in range(2, n+1):
#     dp.append(dp[i-1] + dp[i-2])
# result = (dp[n-1] + dp[n-1]+dp[n-2]) * 2
# print(result)

n = int(input())

dp = [4, 6]

for i in range(2, n+1):
    dp.append(dp[i-1] + dp[i-2])
print(dp[n-1])
