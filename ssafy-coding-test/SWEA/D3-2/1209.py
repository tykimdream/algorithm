for tc in range(1, 11):
    t = int(input())
    arr = []
    for _ in range(100):
        arr.append(list(map(int, input().split())))

    result = []
    for i in range(100):
        result.append(sum(arr[i]))

    for i in range(100):
        total = 0
        for j in range(100):
            total += arr[j][i]
        result.append(total)

    total = 0
    for i in range(100):
        total += arr[i][i]
    result.append(total)

    total = 0
    for i in range(99, -1,  -1):
        total += arr[99 - i][i]
    result.append(total)
    print("#{} {}".format(tc, max(result)))