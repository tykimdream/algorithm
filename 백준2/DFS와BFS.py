from collections import deque

n, m, k = map(int, input().split())
graph = [[] * n for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [False] * (n+1)


def dfs(v):
    visited[v] = True
    print(v, end=" ")
    graph[v].sort()
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


dfs(k)

visited = [False] * (n+1)
q = deque()


def bfs(v):
    q.append(v)
    visited[v] = True
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


print()
bfs(k)
