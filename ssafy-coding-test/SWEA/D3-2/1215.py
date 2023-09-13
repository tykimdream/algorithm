for tc in range(1, 11):
    n = int(input())
    arr = []
    for _ in range(8):
        arr.append(list(map(str, input())))

    count = 0
    for i in range(8):
        for j in range(8 - n + 1):
            temp = []
            for k in range(n):
                temp.append(arr[i][j+k])
            if temp == list(reversed(temp)):
                count += 1
    for i in range(8 - n + 1):
        for j in range(8):
            temp = []
            for k in range(n):
                temp.append(arr[i+k][j])
            if temp == list(reversed(temp)):
                count += 1

    print("#{} {}".format(tc, count))