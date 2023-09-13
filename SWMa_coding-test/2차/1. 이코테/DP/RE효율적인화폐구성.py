n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(int(input()))

# 10001의 경우 만들 수 없다는 뜻
dp = [10001] * (m+1)
dp[0] = 0

for i in range(n):
    for j in range(arr[i], m+1):
        if dp[j-arr[i]] != 10001:  # i - k 원을 만드는 방법이 존재하는 경우
            dp[j] = min(dp[j], dp[j-arr[i]]+1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])
