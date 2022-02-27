# 에라토스테네스의 체 알고리즘 활용
# import math
# n = int(input("타겟 넘버를 입력하시요 : "))
# arr = []

# for i in range(n):
#     arr.append(int(i))
# print(arr)
# for i in range(2, int(math.sqrt(n))+1):
#     j = 2
#     while i * j <= n:
#         arr.pop(i*j)
#         j += 1

# print(arr)

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
