import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 거리 0, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


n, m, start = map(int, input().split())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for i in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보 입력 받기
for i in range(m):
    x, y, z = map(int, input().split())
    # x번 노드에서 y번 노드로 가는 비용이 z라는 의미
    graph[x].append((y, z))

# 다익스트라 수행
dijkstra(start)

# 도달할 수 있는 노드의 갯수
count = 0
# 그 중 가장 멀리 있는 거리
max_distance = 0
for d in distance:
    if d != 1e9:
        count += 1
        max_distance = max(max_distance, d)

print(count-1, max_distance)
