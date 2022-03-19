# import heapq
# import sys
# input = sys.stdin.readline
# INF = int(1e9)
# n, m = map(int, input().split())

# ward = list(map(int, input().split()))
# spot = []

# # 넥서스를 제외한 와드 박혀있는 노드 인덱스 저장
# for i in range(len(ward)-1):
#     if ward[i] == 1:
#         spot.append(i)

# # print(spot)
# graph = [[] for _ in range(n)]

# for _ in range(m):
#     a, b, c = map(int, input().split())
#     if b in spot or a in spot:
#         continue
#     else:
#         graph[a].append((b, c))
#         graph[b].append((a, c))

# # print()
# # print(graph)
# # print()

# distance = [INF] * n


# def dijkstra(start):
#     q = []
#     heapq.heappush(q, (0, start))
#     distance[start] = 0
#     while q:
#         dist, now = heapq.heappop(q)
#         if distance[now] < dist:
#             continue
#         for i in graph[now]:
#             cost = dist + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))


# dijkstra(0)

# if distance[n-1] == INF:
#     print(-1)
# else:
#     print(distance[n-1])

# # 그래프 이어주는 부분에 무방향인거 인지안하고
# # 단방향으로 이어줘서 12가 안나오고 13이 나왔음

# import heapq
# import sys
# input = sys.stdin.readline
# INF = int(1e9)
# n, m = map(int, input().split())

# ward = list(map(int, input().split()))
# ward[-1] = 0
# # print(ward)
# graph = [[] for _ in range(n)]

# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))
#     graph[b].append((a, c))

# # print()
# # print(graph)

# distance = [INF] * n


# def dijkstra():
#     q = []
#     heapq.heappush(q, (0, 0))
#     distance[0] = 0
#     while q:
#         dist, now = heapq.heappop(q)
#         if distance[now] < dist:
#             continue
#         for i in graph[now]:
#             cost = dist + i[1]
#             if cost < distance[i[0]] and ward[i[0]] == 0:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))


# dijkstra()

# if distance[n-1] == INF:
#     print(-1)
# else:
#     print(distance[n-1])

# # 그래도 시간 초과가 나와서 spot을 삭제하고 ward값을 그대로 이용

# import heapq
# import sys
# input = sys.stdin.readline
# INF = int(1e9)
# n, m = map(int, input().split())

# ward = list(map(int, input().split()))
# ward[-1] = 0
# # print(ward)
# graph = [[] for _ in range(n)]

# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))
#     graph[b].append((a, c))

# # print()
# # print(graph)

# distance = [INF] * n

# q = []
# heapq.heappush(q, (0, 0))
# distance[0] = 0
# while q:
#     dist, now = heapq.heappop(q)
#     if distance[now] < dist:
#         continue
#     for next, cost in graph[now]:
#         next_cost = dist + next
#         if cost < distance[next] and ward[next] == 0:
#             distance[next] = next_cost
#             heapq.heappush(q, (next_cost, next))


# if distance[n-1] == INF:
#     print(-1)
# else:
#     print(distance[n-1])

import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize
n, m = map(int, input().split())

ward = list(map(int, input().split()))
ward.pop()
ward.append(0)
# print(ward)
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# print()
# print(graph)

distance = [INF] * n

q = []
heapq.heappush(q, (0, 0))
distance[0] = 0

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for next, cost in graph[now]:
        next_cost = dist + cost
        if next_cost < distance[next] and ward[next] == 0:
            distance[next] = next_cost
            heapq.heappush(q, (next_cost, next))

if distance[n-1] == INF:
    print(-1)
else:
    print(distance[n-1])
