import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

# 버스 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


# a - b로 가는 비용 계산
a, b = map(int, input().split())

dijkstra(a)
print(distance[b])
