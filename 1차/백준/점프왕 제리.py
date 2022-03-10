n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[False] * n for _ in range(n)]

dx = [1, 0]
dy = [0, 1]
queue = [[0, 0]]


def bfs():
    while queue:
        x, y = queue.pop(0)
        if graph[x][y] == -1:
            return "HaruHaru"
        jump = graph[x][y]
        for i in range(2):
            nx = x + dx[i] * jump
            ny = y + dy[i] * jump
            if (0 <= nx < n and 0 <= ny < n):
                # if graph[nx][ny] != -1:
                if visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append([nx, ny])
    return "Hing"


print(bfs())
