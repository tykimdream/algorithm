INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for i in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

# 각 간선에 대한 정보를 입력받는다.
for _ in range(m):
    # a - b 로 가는 c 비용
    a, b, c = map(int, input().split())

    graph[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INF", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
