T = int(input())

for tc in range(1, T+1):
    arr = []
    for _ in range(5):
        arr.append(input())

    max_len = 0
    for i in arr:
        if len(i) > max_len:
            max_len = len(i)

    print("#{}".format(tc), end=" ")
    for i in range(max_len):
        for j in range(5):
            if i < len(arr[j]):
                print(arr[j][i], end='')
    print()