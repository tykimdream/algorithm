# https://www.acmicpc.net/problem/15990

t = int(input())
dp = [0] * 100000
dp[1] = 1
dp[2] = 1
dp[3] = 3
# 4: 1+2+1 1+3 3+1
dp[4] = 3
# 5: 1+3+1, 2+1+2, 3+2, 2+3
dp[5] = 4
# 6: 1+2+3, 1+3+2, 2+1+3, 2+3+1, 3+2+1
# 1+2+1+2, 2+1+2+1
dp[6] = 7
# 7: 2+3+2, 3+1+3,
# for i in range(100000):


for _ in range(t):
    n = int(input())
