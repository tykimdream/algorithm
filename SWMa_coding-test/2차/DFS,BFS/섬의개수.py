# https://www.acmicpc.net/problem/4963
from collections import deque

# 방향벡터 설정 상하좌우 우상 우하 좌상 좌하
dx = [-1, 1, 0, 0, -1, 1, 1, -1]
dy = [0, 0, -1, 1, 1, 1, -1, -1]


def bfs(x, y):
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == 1:
                arr[nx][ny] = 0
                q.append([nx, ny])


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        exit()
    arr = []
    for i in range(h):
        arr.append(list(map(int, input().split())))
    # print(arr)

    count = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                arr[i][j] = 0
                bfs(i, j)
                count += 1

    print(count)
