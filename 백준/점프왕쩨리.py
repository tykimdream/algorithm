# 16173
n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

# 아래와 오른쪽만 이동 가능
dx = [1, 0]
dy = [0, 1]


def bfs(graph, x, y):
    if x < 0 or x > n or y < 0 or y > n:
        return False
    if graph[x][y] != -1:
        bfs(graph, x+1, y)
        bfs(graph, x, y+1)
    else:
        print("HaruHaru")
