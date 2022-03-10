# from collections import deque
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

# 인접 행렬 리스트 제작
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 확인
# print(graph)

visited = [False] * (n+1)


# def bfs(v):
#     q = deque([v])
#     visited[v] = True
#     while q:
#         v = q.popleft()
#         for i in graph[v]:
#             if not visited[i]:
#                 visited[i] = True
#                 q.append(i)


def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


count = 0
for i in range(1, n+1):
    if not visited[i]:
        count += 1
        dfs(i)


print(count)
