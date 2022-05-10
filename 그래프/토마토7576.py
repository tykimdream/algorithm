from collections import deque
m, n = map(int, input().split())

graph = []

# 도마도 판을 입력받는다.
for _ in range(n):
    graph.append(list(map(int, input().split())))

# print(graph)


# 방향 벡터 설정(상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()

# 토마토가 있는 위치 리턴
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append([i, j])


def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append([nx, ny])


bfs()
result = 0
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    result = max(result, max(i))

print(result-1)
