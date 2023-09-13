from collections import deque


def dfs(graph, visited, v):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, visited, i)


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]


visited = [False] * 9

print("dfs 결과 : ", end=' ')
dfs(graph, visited, 1)


# def bfs(graph, visited, start):
#     q = deque([start])
#     visited[start] = True
#     while q:
#         v = q.popleft()
#         print(v, end=' ')
#         for i in graph[v]:
#             if not visited[i]:
#                 q.append(i)
#                 visited[i] = True


# def bfs(graph, visited, start):
#     queu = deque([start])
#     visited[start] = True
#     while queu:
#         v = queu.popleft()
#         print(v, end=' ')
#         for i in graph[v]:
#             if not visited[i]:
#                 queu.append(i)
#                 visited[i] = True


def bfs(graph, visited, start):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]


visited = [False] * 9

print("\nbfs 결과 : ", end=' ')
bfs(graph, visited, 1)


def bfs(graph, visited, start):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


visited = [False] * 9

print("\nbfs2 결과 : ", end=' ')
bfs(graph, visited, 1)
