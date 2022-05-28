T = int(input())

for tc in range(1, T+1):
    n, r = map(int, input().split())

    top, bottom = 1, 1

    for i in range(n, n - r, -1):
        top *= i
    for i in range(1, r + 1):
        bottom *= i

    print("#{} {}".format(tc, (top // bottom) % 1234567891))
