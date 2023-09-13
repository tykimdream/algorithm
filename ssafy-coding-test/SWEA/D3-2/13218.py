T = int(input())

for tc in range(1, T+1):
    n = int(input())
    if n < 3:
        result = 0
    else:
        result = n // 3

    print("#{} {}".format(tc, result))