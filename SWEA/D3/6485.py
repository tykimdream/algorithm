T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = [0] * 5001
    for _ in range(n):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            arr[i] += 1

    p = int(input())
    stop = []
    for _ in range(p):
        stop.append(int(input()))

    print("#{}".format(tc), end = ' ')
    for i in stop:
        print(arr[i], end = ' ')
    print()