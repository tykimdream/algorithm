# 14916

# n = int(input())
# dp = [-1]*(n+1)
# dp[0] = 0
# for i in range(1, n+1):
#     if i >= 2 and dp[i-2] > -1:
#         if dp[i] == -1:
#             dp[i] = (dp[i-2]+1)
#         else:
#             min(dp[i-2]+1, dp[i])
#     if i >= 5 and dp[i-5] > -1:
#         if dp[i] == -1:
#             dp[i] = (dp[i-5]+1)
#         else:
#             min(dp[i-5]+1, dp[i])
# print(dp[n])

# n = int(input())
# dp = [-1] * (n+1)
# dp[0] = 0
# for i in range(1, n+1):
#     if i >= 2 and dp[i-2] > -1:
#         if dp[i] == -1:
#             # 기존 데이터가 없는 경우
#             dp[i] = (dp[i-2]+1)
#         else:
#             # 기존 데이터가 있는 경우
#             # 작은 것으로 업데이트한다.
#             dp[i] = min(dp[i-2] + 1, dp[i])
#     if i >= 5 and dp[i-5] > -1:
#         if dp[i] == -1:
#             dp[i] = (dp[i-5] + 1)
#         else:
#             dp[i] = min(dp[i-5]+1, dp[i])

# print(dp[n])

n = int(input())
dp = [-1] * (n+1)
dp[0] = 0

for i in range(1, n+1):
    if i >= 2 and dp[i-2] > -1:
        if dp[i] == -1:
            dp[i] = dp[i-2] + 1
        else:
            dp[i] = min(dp[i-2] + 1, dp[i])
    if i >= 5 and dp[i-5] > -1:
        if dp[i] == -1:
            dp[i] = dp[i-5] + 1
        else:
            dp[i] = min(dp[i-5]+1, dp[i])

print(dp[n])
