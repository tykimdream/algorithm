# https://www.acmicpc.net/problem/11053
# 다시 풀어보기

n = int(input())
arr = list(map(int, input().split()))

# dp = [1] * n

# for i in range(n):
#     if arr[i] > arr[i-1]:
#         dp[i] = max(dp) + 1

# print(max(dp))


dp = [1] * n
for i in range(1, n):
    for j in range(0, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
