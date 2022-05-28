n, k = map(int, input().split())
weight = []
value = []

for _ in range(n):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)

dp = [[0 for x in range(k + 1)] for y in range(n+1)]

# 물건의 수를 무게(1~k)만큼 반복
for i in range(n + 1):
    for j in range(k + 1):
        if i == 0 or j == 0:
            dp[i][j] == 0
        elif weight[i - 1] < j:
            dp[i][j] = max(value[i - 1] + dp[i - 1][j - weight[i - 1]], dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[i][j])

