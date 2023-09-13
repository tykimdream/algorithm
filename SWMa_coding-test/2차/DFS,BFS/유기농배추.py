# https://www.acmicpc.net/problem/1012
from collections import deque

t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1:
                    arr[nx][ny] = 0
                    q.append([nx, ny])


for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0] * (m) for i in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1
    # 입력된 배추의 위치 확인
    # print(arr)
    count = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                arr[i][j] = 0
                bfs(i, j)
                count += 1
    print(count)
