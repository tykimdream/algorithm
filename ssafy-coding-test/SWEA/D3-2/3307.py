T = int(input())

for tc in range(1, T+1):
    size = int(input())
    arr = list(map(int, input().split()))

    dp = [1] * size
    for i in range(size):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    print("#{} {}".format(tc, max(dp)))