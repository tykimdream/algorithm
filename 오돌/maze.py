n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
print("입력받은 미로 : ", arr)
# 상 하 우 우하
dx = [-1, 1, 0, 1]
dy = [0, 0, 1, 1]

# 상

visited = [[False] * m for _ in range(n)]
result = [[0] * m for _ in range(n)]
result[0][0] = 1


def maze(x, y):
    for i in range(n):
        print(result[i])
    print()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 0 and visited[nx][ny] == False:
            result[nx][ny] = result[nx][ny] + result[x][y]
            visited[nx][ny] = True
        maze(nx, ny)
    # visited[nx][ny] = False


maze(0, 0)
print("처리한 미로 : ")

for i in range(n):
    print(result[i])

# from collections import deque
# n, m = map(int, input().split())
# arr = []
# for _ in range(n):
#     arr.append(list(map(int, input().split())))
# print("입력받은 미로 : ", arr)
# # 상 하 우 우하
# dx = [-1, 1, 0, 1]
# dy = [0, 0, 1, 1]

# # 상

# visited = [[False] * m for _ in range(n)]
# result = [[0] * m for _ in range(n)]
# result[0][0] = 1


# def maze(x, y):

#     q = deque()
#     q.append((x, y))
#     while q:
#         visited = [[False] * m for _ in range(n)]
#         x, y = q.popleft()
#         for i in range(n):
#             print(result[i])
#         print()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 0 and visited[nx][ny] == False:
#                 result[nx][ny] = result[nx][ny] + result[x][y]
#                 visited[nx][ny] = True
#                 q.append((nx, ny))
#     # visited[nx][ny] = False


# maze(0, 0)
# print("처리한 미로 : ")

# for i in range(n):
#     print(result[i])
