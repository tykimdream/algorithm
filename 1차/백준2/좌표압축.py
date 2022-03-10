# 18870

# 시간 초과 n^2
# n = int(input())
# arr = list(map(int, input().split()))
# corrd = sorted(list(set(arr)))

# print(corrd)
# for i in arr:
#     print(corrd.index(i), end=" ")


n = int(input())
arr = list(map(int, input().split()))
corrd = sorted(list(set(arr)))
dic = {corrd[i]: i for i in range(len(corrd))}

for i in arr:
    print(dic[i], end=" ")


# n = int(input())
# arr = list(map(int, input().split()))
# corrd = sorted(list(set(arr)))
# li = []
# for i, v in enumerate(corrd):
#     li.append((i, v))

# print(li)

# # for i in arr:
# #     print(li[i][0], end=" ")
