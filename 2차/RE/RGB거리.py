# https://www.acmicpc.net/problem/1149

n = int(input())
color = []
for _ in range(n):
    color.append(list(map(int, input().split())))
# print(color)

for i in range(1, n):
    color[i][0] = min(color[i-1][1], color[i-1][2]) + color[i][0]
    color[i][1] = min(color[i-1][0], color[i-1][2]) + color[i][1]
    color[i][2] = min(color[i-1][0], color[i-1][1]) + color[i][2]
print(min(color[n-1]))
