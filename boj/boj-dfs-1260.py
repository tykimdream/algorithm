from collections import deque

n, m, k = map(int, input().split())

arr = [[] for i in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(1, n + 1):
    arr[i].sort()


def dfs(arr, visited, v):
    visited[v] = True
    print(v, end=' ')
    for i in arr[v]:
        if not visited[i]:
            dfs(arr, visited, i)


def bfs(arr, visited, v):
    que = deque([v])
    visited[v] = True
    while que:
        t = que.popleft()
        print(t, end=' ')
        for i in arr[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True


visited = [False] * (n + 1)
dfs(arr, visited, 1)
print()
visited = [False] * (n + 1)
bfs(arr, visited, 1)
