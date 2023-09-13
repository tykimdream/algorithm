# n = int(input())
# order = input().split()

# corrd = [1,1]

# for op in order:
#     if op == 'D':
#         if corrd[0] + 1 <= n:
#             corrd[0]+=1
#     if op == 'L':
#         if corrd[0] - 1 >= 0:
#             corrd[0] -=1
#     if op == 'L':
#         if corrd[1] - 1 >= 0:
#             corrd[1] -=1
#     if op == 'R':
#         if corrd[1] + 1 <= n:
#             corrd[1] +=1

# print(corrd)

n = int(input())
order = input().split()
x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']

for op in order:
    for i in range(4):
        if op == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x = nx
    y = ny

print(x, y)