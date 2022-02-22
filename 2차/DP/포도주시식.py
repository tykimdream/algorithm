# https://www.acmicpc.net/problem/2156
# 인덱스 오류 3번 발생 why?


# ===========================================
# n = int(input())
# wine = []

# for i in range(n):
#     wine.append(int(input()))

# dp = [0] * (n+1)
# dp[0] = wine[0]
# dp[1] = dp[0] + wine[1]
# dp[2] = max(dp[1], wine[1]+wine[2], wine[2]+wine[0])

# for i in range(3, n):
#     dp[i] = max(dp[i-3] + wine[i-1] + wine[i],
#                 dp[i-2] + wine[i], dp[i-1])
# # print(dp)
# print(max(dp))

# ===========================================
# 정답
# n = int(input())
# wine = [0] * 10000

# for i in range(n):
#     wine[i] = int(input())

# dp = [0] * (10000)
# dp[0] = wine[0]
# dp[1] = dp[0] + wine[1]
# dp[2] = max(dp[1], wine[1]+wine[2], wine[2]+wine[0])

# for i in range(3, n):
#     dp[i] = max(dp[i-3] + wine[i-1] + wine[i],
#                 dp[i-2] + wine[i], dp[i-1])
# # print(dp)
# print(max(dp))

# ===========================================
# 인덱스 에러
# n = int(input())

# wine = []
# for _ in range(n):
#     wine.append(int(input()))

# dp = [0] * (n+1)

# dp[0] = wine[0]
# dp[1] = dp[0] + wine[1]
# dp[2] = max(wine[1]+wine[2], wine[0]+wine[2], dp[1])

# for i in range(3, n):
#     dp[i] = max(dp[i-3]+wine[i-1]+wine[i], dp[i-2]+wine[i], dp[i-1])

# print(max(dp))

# ===========================================
n = int(input())

wine = []
for _ in range(n):
    wine.append(int(input()))

dp = []

dp.append(wine[0])
if n > 1:
    dp.append(dp[0] + wine[1])
    if n > 2:
        dp.append(max(wine[1]+wine[2], wine[0]+wine[2], dp[1]))
        if n > 3:
            for i in range(3, n):
                dp.append(max(dp[i-3]+wine[i-1]+wine[i],
                          dp[i-2]+wine[i], dp[i-1]))

print(max(dp))
