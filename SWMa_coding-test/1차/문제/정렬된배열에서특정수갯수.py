# n, x = map(int, input().split())
# target = list(map(int, input().split()))

# count = 0
# for i in range(n):
#     if target[i] == x:
#         count += 1

# print(count)

from bisect import bisect_left, bisect_right
import random
# n, x = map(int, input().split())
# target = list(map(int, input().split()))
# count = 0


# def range_gap(arr, left, right):
#     left = bisect_left(arr, left)
#     right = bisect_right(arr, right)
#     return right - left


# print(range_gap(target, x, x))


n = int(input())


def gapping(arr, value):
    left = bisect_left(arr, value)
    right = bisect_right(arr, value)
    return right - left


arr = []
for i in range(10001):
    arr.append(random.randrange(1, 10))

arr.sort()

print(n, "의 갯수 :", gapping(arr, n))
