from collections import deque
import sys
sys.setrecursionlimit(10**9)
n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

q = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q.append([0, 0])


def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n and 0 <= ny < m) and graph[nx][ny] != 0:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append([nx, ny])


bfs()
print(graph[n-1][m-1])
