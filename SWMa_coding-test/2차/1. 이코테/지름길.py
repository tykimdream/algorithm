# import heapq
# import sys
# input = sys.stdin.readline

# n, d = map(int, input().split())

# graph = [[] for _ in range(10001)]

# for _ in range(n):
#     a, b, c = map(int, input().split())
#     graph[a].append([b, c])

# dis = [i for i in range(d+1)]


# for i in range(d+1):
#     if i != 0:
#         dis[i] = min(dis[i], dis[i-1]+1)
#     for w, e in graph[i]:
#         if e <= d and dis[e] > w + dis[i]:
#             dis[e] = w + dis[i]

# print(dis[d])


N, D = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(N)]
dis = [i for i in range(D+1)]
for i in range(D+1):
    if i > 0:
        dis[i] = min(dis[i], dis[i-1]+1)
    for s, e, d in li:
        if i == s and e <= D and dis[i]+d < dis[e]:
            dis[e] = dis[i]+d
print(dis[D])
