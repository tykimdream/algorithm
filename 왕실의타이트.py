move = input()
x = ord(move[0]) - ord('a') + 1
y = int(move[1])

dx = [-2, -1,  1,  2, 2, 1, -2, -1]
dy = [-1, -2, -2, -1, 1, 2,  1, 2]

pos = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
        pos += 1

print(pos)
