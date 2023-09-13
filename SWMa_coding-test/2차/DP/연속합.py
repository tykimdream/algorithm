# https://www.acmicpc.net/problem/1912
# n = int(input())

# arr = list(map(int, input().split()))
# dp = [0 for _ in range(n+1)]
# # dp[0] = arr[0]
# # print(arr, dp)

# for i in range(1, n-1):
#     dp[i] = max(dp[i]+arr[i+1], arr[i+1])
# print(dp)
# print(max(dp))


# n = int(input())

# arr = list(map(int, input().split()))
# dp = []
# dp.append(arr[0])
# # print(arr, dp)

# for i in range(n-1):
#     dp.append(max(dp[i]+arr[i+1], arr[i+1]))
# print(dp)
# print(max(dp))

from re import L


n = int(input())
arr = list(map(int, input().split()))

dp = []
dp.append(arr[0])

for i in range(n-1):
    dp.append(max(dp[i] + arr[i+1], arr[i+1]))

print(max(dp))
