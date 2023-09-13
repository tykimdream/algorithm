T = int(input())

for tc in range(1, T+1):
    str1, str2 = map(str, input().split())

    dp = [[0] * len(str2) for i in range(len(str1))]

    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    print("#{} {}".format(tc, dp[-1][-1]))
