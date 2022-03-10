n = int(input())

command = list((input().split()))
x, y = 1, 1

for i in command:
    if i == 'R':
        if x + 1 <= n:
            x += 1
    if i == 'L':
        if x-1 >= 1:
            x -= 1
    if i == 'U':
        if y-1 >= 1:
            y -= 1
    if i == 'D':
        if y+1 <= n:
            y += 1

print(y, x)
