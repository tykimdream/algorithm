from collections import deque

m,n = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))
print(graph)
q = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i,j))


dx = [-1,1,0,0]
dy = [0,0,-1,1]
print(q)
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y] + 1
            q.append((nx, ny))


max = 1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            exit()
        else:
            if graph[i][j] > max:
                max = graph[i][j]

print(max-1)