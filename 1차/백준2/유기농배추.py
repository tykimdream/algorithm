from collections import deque

q = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
                arr[nx][ny] = 0
                q.append([nx, ny])


T = int(input())

for i in range(T):
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    count = 0
    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                bfs(i, j)
                count += 1
    print(count)
