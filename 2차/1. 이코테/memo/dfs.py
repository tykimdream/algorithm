from collections import deque
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()


def dfs(graph, visited, v):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, visited, i)


def bfs(graph, visited, v):
    q = deque()
    visited[v] = True
    q.append(v)
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append(i)


visited = [False] * (n+1)
bfs(graph, visited, v)

visited = [False] * (n+1)
dfs(graph, visited, v)
