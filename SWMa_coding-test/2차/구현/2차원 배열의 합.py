# https://www.acmicpc.net/problem/2167

n, m = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))


dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = arr[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]

# dp 배열에 누적 합 저장
# print(dp)

case = int(input())
for i in range(case):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1])
