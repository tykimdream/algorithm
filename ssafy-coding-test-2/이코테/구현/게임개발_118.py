n, m = map(int, input().split())
x, y, dir = map(int, input().split())

visited = [[0] * m for _ in range(n)]
visited[x][y] = 1

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 1
turn_time = 0

while True:
    dir -=1
    if dir == -1:
        dir = 3
    nx = x + dx[dir]
    ny = y + dx[dir]
    # 회전한 정면이 가보지않은 칸인 경우 이동
    if visited[nx][ny] == 0 and arr[nx][ny] == 0:
        visited[nx][ny] = 1
        x = nx
        y = ny
        count +=1
        turn_time = 0
        continue
    # 회전한 정면이 가본 칸이거나 바다인 경우
    else:
        turn_time +=1
    if turn_time == 4:
        nx = x - dx[dir]
        ny = y - dy[dir]
        if arr[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)