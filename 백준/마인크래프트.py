# 18111
# # 가로, 세로, 인벤토리 아이템 수
# n, m, b = map(int, input().split())

# ground = []

# for _ in range(n):
#     ground.append(list(map(int, input().split())))

# # 평지화 하는데
# # 1. 땅을 판다 - 2초 소요, 아이템 1개 증가
# # 2. 땅을 메꾼다 - 1초 소요, 아이템 1개 소모

# max = max(max(ground))
# min = min(min(ground))

# # 1번 액션의 경우 코스트
# cost_1 = 0
# # 2번 액션의 경우 코스트
# cost_2 = 0

# # 1번 액션의 코스트 계산
# for i in range(n):
#     for j in range(m):
#         cost_1 += ground[i][j] - min


# # 2번 액션의 코스트 계산
# for i in range(n):
#     for j in range(m):
#         cost_2 += max - ground[i][j]

# time_1 = cost_1 * 2
# time_2 = cost_2

# if time_1 > time_2 and cost_2 <= b:
#     print(time_2, max)
# else:
#     print(time_1, min)

# 실패1. 중간 값을 생각 못했다.
# 2 2 0
# 256 256
# 0 0
# 이 경우 796 128에 높이가 맞춰지면되는데 1024 0이 출력된다.

# 인벤토리에 넣다 빼는것을 고려할 것

import sys

N, M, B = map(int, sys.stdin.readline().split())
li = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
time, height = 9223372036854775807, 0
for h in range(257):
    bot = top = 0
    for i in range(N):
        for j in range(M):
            if li[i][j] < h:
                bot += h-li[i][j]
            else:
                top += li[i][j]-h
    if bot > top + B:
        continue
    t = bot + top*2
    if t <= time:
        time = t
        height = h
print(time, height)
