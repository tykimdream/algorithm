# https://www.acmicpc.net/problem/1012

from collections import deque

# 방향 벡터 선언
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()


def bfs(x, y):
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and dp[nx][ny] == 1:
                dp[nx][ny] = 0
                q.append([nx, ny])


T = int(input())
# 밭을 입력받는다.
for i in range(T):
    m, n, k = map(int, input().split())
    dp = [[0] * m for i in range(n)]
    count = 0
    for i in range(k):
        x, y = map(int, input().split())
        dp[y][x] = 1
    for x in range(n):
        for y in range(m):
            if dp[x][y] == 1:
                bfs(x, y)
                dp[x][y] = 0
                count += 1
    print(count)
