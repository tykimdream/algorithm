T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())

    b = n - m
    a = m - b

    print("#{} {} {}".format(tc, a, b))