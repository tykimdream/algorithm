# t = int(input())

# for _ in range(t):
#     n, m = map(int, input().split())
#     dp = [1, 1+n]
#     for i in range(2, m+1):
#         dp.append(dp[i-1]+dp[i-2]+n)
#     print(dp[m])

T = int(input())

for _ in range(T):
    m, n = map(int, input().split())
    answer = 1
    k = n - m

    while n > k:
        answer *= n
        n -= 1
    while m > 1:
        answer = answer // m
        m -= 1

    print(answer)
