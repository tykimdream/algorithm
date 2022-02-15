from tkinter import E


n, m = map(int, input().split())
d = [[0] * m for _ in range(n)]

x, y, direction = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

d[x][y] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


# 시뮬레이션 시작
step = 1
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and arr[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        step += 1
        turn_time = 0
    else:
        turn_time += 1
    # 4 방향 모두 진행 불가한 경우, backward
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if arr[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(step)
