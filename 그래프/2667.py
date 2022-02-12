# 22.02.12 2667 단지번호붙이기
# <그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
# 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
# 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다.
# <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고,
# 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

# Sol. 1 이상한 값 나옴
# 방향 벡터 설정 상하좌우
# dx = [0, 0, -1, 1]
# dy = [1, -1, 0, 0]


# def dfs(x, y):
#     graph[x][y] = 0
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
#             dfs(nx, ny)
#         else:
#             return False


# n = int(input())
# graph = []

# for i in range(n):
#     graph.append(list(map(int, input())))

# dong = [0] * 15

# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 1:
#             dfs(i, j)
#             dong[i] += 1
# print(dong)

# Sol. 2
# 방향 벡터 설정 상하좌우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False


n = int(input())
graph = []
dong = []

for i in range(n):
    graph.append(list(map(int, input())))

count = 0
result = 0

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            dong.append(count)
            result += 1
            count = 0

print(len(dong), dong)
