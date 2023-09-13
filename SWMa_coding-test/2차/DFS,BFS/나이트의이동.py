# https://www.acmicpc.net/problem/7562
from collections import deque
t = int(input())

# 방향 벡터 설정 8가지 경우
# 좌상좌, 좌상상, 우상상, 우상우, 우하우, 우하하, 좌하하, 좌하좌
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

for _ in range(t):
    # 체스판 사이즈 입력받기
    size = int(input())
    arr = [[0] * size for _ in range(size)]

    # 초기 시작 위치
    x, y = map(int, input().split())

    # 타겟 위치
    tx, ty = map(int, input().split())

    def bfs(x, y):
        q = deque()
        arr[x][y] = 1
        q.append((x, y))
        while q:
            x, y = q.popleft()
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < size and 0 <= ny < size and arr[nx][ny] == 0:
                    arr[nx][ny] = arr[x][y] + 1
                    q.append((nx, ny))

    bfs(x, y)
    # print(arr)
    print(arr[tx][ty]-1)
    # for i in range(size):
    #     for j in range(size):
    #         if arr[i][j] == 0:
    #             arr[i][j] = 1
    #             bfs(i, j)
