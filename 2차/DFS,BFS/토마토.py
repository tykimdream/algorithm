# https://www.acmicpc.net/problem/7576
from collections import deque
m, n = map(int, input().split())
arr = []

# 현재 상태 입력받기
for _ in range(n):
    arr.append(list(map(int, input().split())))

# 하루 지날 때마다 숫자로 표기
# 마지막에 가장 큰 수를 출력하면 다 된 것
# 단 감염이 안되는 경우가 있으면 -1 출력

# 최초 토마토 위치 받기
q = deque()

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i, j))

# 방향 벡터 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    while q:
        # print(arr)
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx, ny))


bfs()
max = 1
# 익지 않은 토마토와 익은 날짜(MAX) 추출
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            print(-1)
            exit()
        if arr[i][j] > max:
            max = arr[i][j]

print(max-1)
