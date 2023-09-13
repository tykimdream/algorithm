# https://www.acmicpc.net/problem/1003

t = int(input())

for _ in range(t):
    n = int(input())
    if n == 0:
        print(1, 0)
        continue
    dp_0 = [0] * (n+1)
    dp_1 = [0] * (n+1)
    dp_0[0] = 1
    dp_1[1] = 1

    for i in range(2, n+1):
        dp_0[i] = dp_0[i-1] + dp_0[i-2]
        dp_1[i] = dp_1[i-1] + dp_1[i-2]
    print(dp_0[n], dp_1[n])
    # print(dp_0, dp_1)
