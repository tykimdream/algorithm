a = input().split('-')

num = []

for i in a:
    local = 0
    temp = i.split('+')
    for j in temp:
        local += int(j)
    num.append(local)

print(-(sum(num) - num[0] * 2))