T = int(input())

for tc in range(1, T+1):
    a, b, c = map(int, input().split())
    if a == b == c:
        result = a
    else:
        if a == b:
            result = c
        elif a == c:
            result = b
        elif b == c:
            result = a

    print("#{} {}".format(tc, result))