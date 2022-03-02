# 1260
from collections import deque
n, m, v = map(int, input().split())
graph = [[] * n for _ in range(n+1)]

# 인접행렬리스트로 입력 받음
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 인접행렬리스트 확인
# print(graph)

visited = [False] * (n+1)


def dfs(start):
    visited[start] = True
    print(start, end=' ')
    graph[start].sort()
    for i in graph[start]:
        if not visited[i]:
            dfs(i)


dfs(v)
print()


visited = [False] * (n+1)


def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        cur = q.popleft()
        print(cur, end=" ")
        for i in graph[cur]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


bfs(v)
