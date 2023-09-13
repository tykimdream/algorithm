# 모든 노드에서 모든 노드로 가는 최단 거리
# 2차원 테이블에 표현
# 구현이 쉽지만 시간 복잡도가 n^3임

INF = int(1e9)

# 노드와 간선의 개수 입력받기
n = int(input())
m = int(input())

# 2차원 리스트를 만들고 무한으로 초기화
graph = [[INF] * (n+1) for i in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용: C
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 수행된 결과를 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("무한", end=' ')
        else:
            print(graph[a][b])
    print()
