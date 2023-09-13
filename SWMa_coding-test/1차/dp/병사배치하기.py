n = int(input())
arr = list(map(int, input().split()))
arr.reverse()

dp = [1] * n

for i in range(n):
    for j in range(0, 1):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))
