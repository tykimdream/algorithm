# # 1388
# n, m = map(int, input().split())

# wood = []
# for i in range(n):
#     wood.append(list(map(str, input())))
# visited = [[0] * m for _ in range(n)]

# dx = [-1, 1]
# dy = [-1, 1]
# queue = [[0, 0]]
# piece = 1


# def bfs(piece):
#     x, y = queue.pop(0)
#     visited[x][y] = piece
#     # 현재 나무의 무늬
#     cur_type = wood[x][y]
#     if cur_type == '-':
#         for i in range(2):
#             nx = x
#             ny = y + dx[i]
#             if 0 <= nx < n and 0 <= ny < m:
#                 if wood[nx][ny] == cur_type:
#                     visited[nx][ny] = piece
#                     queue.append([nx, ny])
#         piece += 1
#     elif cur_type == '|':
#         for i in range(2):
#             nx = x + dx[i]
#             ny = y
#             if 0 <= nx < n and 0 <= ny < m:
#                 if wood[nx][ny] == cur_type:
#                     visited[nx][ny] = piece
#                     queue.append([nx, ny])
#         piece += 1


# bfs(piece)
# print(visited)
# print((max(visited)))

# Sol
n, m = map(int, input().split())

wood = []
for i in range(n):
    wood.append(list(map(str, input())))
answer = 0


def dfs(x, y):
    if wood[x][y] == '|':
        wood[x][y] = 'o'

        for _x in [1, -1]:
            X = x + _x
            if (X > 0 and X < n) and wood[X][y] == '|':
                dfs(X, y)

    if wood[x][y] == '-':
        wood[x][y] = 'o'

        for _y in [1, -1]:
            Y = y + _y
            if (Y > 0 and Y < m) and wood[x][Y] == '-':
                dfs(x, Y)


for i in range(n):
    for j in range(m):
        if wood[i][j] == '|' or wood[i][j] == '-':
            dfs(i, j)
            answer += 1
print(answer)


# N, M = map(int, input().split())

# graph = []
# for i in range(N):
#     graph.append(list(map(str, input())))
# answer = 0


# def dfs(x, y):
#     if graph[x][y] == '|':
#         graph[x][y] = 'o'

#         for _x in [1, -1]:
#             X = x + _x
#             if (X > 0 and X < N) and graph[X][y] == '|':
#                 dfs(X, y)

#     if graph[x][y] == '-':
#         graph[x][y] = 'o'

#         for _y in [1, -1]:
#             Y = y + _y
#             if (Y > 0 and Y < M) and graph[x][Y] == '-':
#                 dfs(x, Y)


# for i in range(N):
#     for j in range(M):
#         if graph[i][j] == '|' or graph[i][j] == '-':
#             dfs(i, j)
#             answer += 1
# print(answer)
