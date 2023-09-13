T = int(input())
print()
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arr = []
    # Map init
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    pos_count = 0
    for i in range(N):
        for j in range(N):
            # 하얀 부분(삽입이 가능한) 발견시 가로 세로 체크
            if arr[i][j] == 1:
                row_count = 0
                col_count = 0
                row = 0
                col = 0
                while j + row < N:
                    if arr[i][j + row] == 0:
                        break
                    else:
                        if arr[i][j + row] == 1:
                            row_count += 1
                    row += 1
                while i + col < N:
                    if arr[i + col][j] == 0:
                        break
                    else:
                        if arr[i + col][j] == 1:
                            col_count += 1
                    col += 1
                if row_count == K:
                    pos_count += 1
                    print("row check: ", i, j)
                if col_count == K:
                    pos_count += 1
                    print("col check", i, j)
    print("#{} {}".format(test_case, pos_count))