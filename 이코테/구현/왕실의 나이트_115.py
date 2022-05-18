start = input()

x = ord(start[0]) - 96
y = int(start[1])

vary = [[-2, -1], [-2, 1], [2, -1], [2, 1],
        [1, -2], [1, 2], [-1, 2], [-1,-2]]

pos = 0

for step in vary:
    nx = x + step[1]
    ny = y + step[0]
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        pos+=1

print(pos)