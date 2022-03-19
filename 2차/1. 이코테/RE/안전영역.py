# # https://www.acmicpc.net/problem/2468
from collections import deque
# 높이가 n일때로 구했음. 이게 아니라 1~n까지 다 해보고 그 중 최대 영역이 되는 걸 찾아야함
# 문제 해석 유념해서 하기.

# n = int(input())
# arr = []

# for _ in range(n):
#     arr.append(list(map(int, input().split())))

# # print(arr)
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]


# def bfs(x, y):
#     q = deque()
#     q.append([x, y])
#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] > n:
#                 arr[nx][ny] = -1
#                 q.append([nx, ny])


# count = 0
# for i in range(n):
#     for j in range(n):
#         if arr[i][j] > n:
#             arr[i][j] = -1
#             bfs(i, j)
#             count += 1

# print(count)

n = int(input())
arr = []
max = 0

for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(n):
        if arr[i][j] > max:
            max = arr[i][j]

# print(arr)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, value, visited):
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] > value and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append([nx, ny])


result = 0
for i in range(max):
    visited = [[0] * n for i in range(n)]
    count = 0
    for j in range(n):
        for k in range(n):
            if arr[j][k] > i and visited[j][k] == 0:
                bfs(j, k, i, visited)
                count += 1
    if result < count:
        result = count

print(result)
