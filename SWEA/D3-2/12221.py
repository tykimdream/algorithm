T = int(input())

for tc in range(1, T+1):
    a, b = map(int, input().split())

    if a <= 9 and b <= 9:
        result = a * b
    else:
        result = -1
    print("#{} {}".format(tc, result))
