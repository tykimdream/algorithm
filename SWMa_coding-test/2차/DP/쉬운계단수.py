# https://www.acmicpc.net/problem/10844

# 틀림 (인덱스 조정)
# t = int(input())
# p = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
# for _ in range(t):
#     n = int(input())
#     for i in range(10, n+1):
#         p.append(p[i-1] + p[i-5])
#     print(p[n-1])

t = int(input())
p = [0 for _ in range(101)]
p[1] = 1
p[2] = 1
p[3] = 1

for i in range(98):
    p[i+3] = p[i] + p[i+1]

for _ in range(t):
    n = int(input())
    print(p[n])
