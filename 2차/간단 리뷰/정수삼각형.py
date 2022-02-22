# https://www.acmicpc.net/problem/1932
# 천천히 다시 풀기

# n = int(input())
# tri = []
# dp = []

# for _ in range(n):
#     tri.append(list(map(int, input().split())))

# for i in range(1, n+1):
#     arr = [0] * i
#     dp.append(arr)

# dp[0][0] = tri[0][0]

# for i in range(1, n):
#     for j in range(i):
#         dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + tri[i][j]

# print(dp)
# print(max(dp[n-1]))

# n = int(input())
# d = []
# for i in range(n):
#     d.append(list(map(int, input().split())))

# for i in range(1, n):
#     for j in range(len(d[i])):
#         if j == 0:
#             d[i][j] = d[i][j]+d[i-1][j]
#         elif j == len(d[i])-1:
#             d[i][j] = d[i][j]+d[i-1][j-1]
#         else:
#             d[i][j] = max(d[i-1][j-1], d[i-1][j])+d[i][j]
# print(max(d[n-1]))


# day 2 틀림, 2중 포문 범위 설정 잘못됨
# n = int(input())
# arr = []
# for i in range(n):
#     arr.append(list(map(int, input().split())))

# for i in range(1, n):
#     for j in range(i):
#         if j == 0:
#             arr[i][j] += arr[i-1][0]
#         elif j == i:
#             arr[i][j] += arr[i-1][i]
#         else:
#             arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])

# print(max(arr[n-1]))

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(len(arr[i])):
        if j == 0:
            arr[i][j] += arr[i-1][j]
        elif j == len(arr[i])-1:
            arr[i][j] += arr[i-1][i-1]
        else:
            arr[i][j] = max(arr[i-1][j-1], arr[i-1][j]) + arr[i][j]

print(max(arr[n-1]))
