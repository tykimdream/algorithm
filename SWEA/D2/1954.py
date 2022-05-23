T = int(input())

for tc in range(1, T+1):
    size = int(input())
    arr = [[0] * size for _ in range(size)]

    row, col = 0, 0
    d = 0

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    for i in range(1, size * size + 1):
        arr[row][col] = i
        row += dr[d]
        col += dc[d]
        if row < 0 or row >= size or col < 0 or col >= size or arr[row][col] != 0:
            row -= dr[d]
            col -= dc[d]
            d = (d+1) % 4
            row += dr[d]
            col += dc[d]

    print("#{}".format(tc))
    for x in range(size):
        for y in range(size):
            print(arr[x][y], end=' ')
        print()
