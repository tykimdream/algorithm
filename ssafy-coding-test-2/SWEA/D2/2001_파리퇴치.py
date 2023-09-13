T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    answer = []
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    # for ed in range(n):
    #     print(arr[ed])
    for i in range(n):
        for j in range(n):
            if i + m <= n and j + m <= n:
                kill = 0
                # print("i, j : ", i, j)
                for a in range(m):
                    # print(a, "set")
                    for b in range(m):
                        kill += arr[i+a][j+b]
                        # print(i+a, j+b, " / ", end = ' ')
                answer.append(kill)
    # print(answer)
    print("#{} {}".format(test_case, max(answer)))