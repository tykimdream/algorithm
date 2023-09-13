from collections import deque
from glob import glob

m, n = map(int, input().split())

# bfs문제
# 1. 인접 행렬을 입력받는다
# 2. BFS를 돌리며 모든 토마토를 익힌다.

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

# print(graph)

q = deque()

# 시작 시점에 익은 토마토를 큐에 삽입
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append([i, j])

# 상하좌우 방향 벡터 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 이렇게 하면 안됨
# count = 0
# def bfs():
#     global count
#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if (0 <= nx < n and 0 <= ny < m) and graph[nx][ny] == 0:
#                 graph[nx][ny] = 1
#                 q.append([nx, ny])
#         count += 1

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n and 0 <= ny < m) and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx, ny])


bfs()
result = 0

for i in graph:
    for j in i:
        if j == 0:
            # 0이 하나라도 존재하면 -1 출력하고 종료
            print(-1)
            exit(0)
    result = max(result, max(i))
print(result - 1)
