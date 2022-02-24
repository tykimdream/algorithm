# https://www.acmicpc.net/problem/1260

from collections import deque

n, m, v = map(int, input().split())
graph = [[] for i in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()


def dfs(graph, visited, v):
    visited[v] = True
    print(v, end=" ")
    # graph[v].sort() 여기서 소팅하지말고 위에서 선언 이후에 소팅하면 더 효율적
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, visited, i)


def bfs(graph, visited, v):
    q = deque([v])
    visited[v] = True
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


visited = [False] * (n+1)
dfs(graph, visited, v)

print()
visited = [False] * (n+1)
bfs(graph, visited, v)
