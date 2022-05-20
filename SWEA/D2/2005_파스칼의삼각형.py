T = int(input())
# print(T)

for case in range(1, T+1):
    size = int(float(input()))
    print("#{}".format(case))
    arr = [[1]]
    for i in range(1, size):
        arr.append([])
        arr[i].append(1)
        for j in range(1, i):
            arr[i].append(arr[i - 1][j - 1] + arr[i - 1][j])
        if size != 0:
            arr[i].append(1)

    for x in range(size):
        for delta in arr[x]:
            print(delta, end=' ')
        print()
