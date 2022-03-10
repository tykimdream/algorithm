# # 아르스토의 체

# import math
# n = int(input())


# def isP(value):
#     std = int(math.sqrt(value))+1
#     dp = []
#     for i in range(value+1):
#         dp.append(i)

#     for i in range(1, std):
#         j = 1
#         while i * j <= value:
#             dp.remove(i*j)
#             j += 1
#     print(dp)


# isP(n)

import math
n = int(input())
arr = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n))+1):
    if arr[i] == True:
        j = 2
        while i*j <= n:
            arr[i*j] = False
            j += 1

for i in range(2, n+1):
    if arr[i] == True:
        print(i, end=' ')
