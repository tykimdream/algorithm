# # 2606

# # 컴퓨터의 수
# n = int(input())

# # 네트워크 엣지의 수
# e = int(input())

# # 컴퓨터 번호 : 연결된 컴퓨터 번호
# com = [[]*n for _ in range(n+1)]

# for _ in range(e):
#     a, b = map(int, input().split())
#     com[a].append(b)
#     com[b].append(a)

# visited = [False] * (n+1)
# cnt = 0


# def dfs(graph, visited, v):
#     global cnt
#     visited[v] = True
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, visited, i)
#             cnt += 1


# dfs(com, visited, 1)
# print(cnt)


n = int(input())
e = int(input())

com = [[] * n for _ in range(n+1)]

# 인접행렬리스트를 만들자
for _ in range(e):
    x, y = map(int, input().split())
    com[x].append(y)
    com[y].append(x)

# print(com)

count = 0
visited = [False] * (n+1)


def dfs(start):
    global count
    visited[start] = True
    for i in com[start]:
        if not visited[i]:
            dfs(i)
            count += 1


dfs(1)
print(count)
