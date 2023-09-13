T = int(input())

for tc in range(1, T+1):
    size = int(input())
    arr = []
    for _ in range(size):
        arr.append(list((input())))

    result = "NO"
    for i in range(size):
        for j in range(size):
            if arr[i][j] == 'o':
                count = 0
                for x in range(5):
                    if j + x < size and arr[i][j + x] == 'o':
                        count += 1
                    if count == 5:
                        result = "YES"
                count = 0
                for x in range(5):
                    if i + x < size and arr[i + x][j] == 'o':
                        count += 1
                    if count == 5:
                        result = "YES"
                count = 0
                for x in range(5):
                    if i + x < size and j + x < size and arr[i + x][j + x] == 'o':
                        count += 1
                    if count == 5:
                        result = "YES"
                count = 0
                for x in range(5):
                    if i + x < size and j - x >= 0 and arr[i + x][j - x] == 'o':
                        count += 1
                        # print("i, j, count: ", x, i - x, j - x, count, end=' // ')
                    if count == 5:
                        result = "YES"
    print("#{} {}".format(tc, result))