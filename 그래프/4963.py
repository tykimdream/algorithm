# 22.02.10 4963

# 정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.

# 한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다.
# 두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다.
# 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.


# 방향 백터 설정 상하좌우, 좌상 우상 우하 좌하
dx = [0, 0, -1, 1, -1, 1, 1, -1]
dy = [-1, 1, 0, 0, -1, -1, 1, 1]


def dfs(x, y):
    island[x][y] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and island[nx][ny] == 1:
            dfs(nx, ny)


def bfs(i, j):
    island[i][j] = 0
    queue = [[i, j]]
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for k in range(8):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < h and 0 <= y < w and island[x][y] == 1:
                island[x][y] = 0
                queue.append([x, y])


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    island = []

    for i in range(h):
        island.append(list(map(int, input().split())))
    result = 0
    for i in range(h):
        for j in range(w):
            if island[i][j] == 1:
                dfs(i, j)
                result += 1

    print(result)


# result = 0
    # for i in range(h):
    #     island.append(list(map(int, input().split())))

    # for i in range(h):
    #     for j in range(w):
    #         if island[i][j] == 1:
    #             bfs(i, j)
    #             result += 1
    # print(result)
