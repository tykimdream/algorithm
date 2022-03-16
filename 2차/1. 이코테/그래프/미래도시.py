# n 회사 개수, m 경로 개수
n, m = map(int, input().split())
# 방문할 회사 k와 x
k, x = map(int, input().split())

# 1 - K - x 로 가는 최단 거리

INF = int(1e9)

graph = [[INF] * (n+1) for _ in range(n+1)]

# for i in range(n+1):
#     graph[i][i] = 0

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0


for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


# print(graph)

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for i in range(1, n+1):
    print(graph[i])

dis = graph[1][k] + graph[k][x]
print(dis)
