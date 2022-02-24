# https://www.acmicpc.net/problem/10815
from bisect import bisect_left, bisect_right
n = int(input())
dic = list(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))


def find(arr, value):
    lix = bisect_left(arr, value)
    rix = bisect_right(arr, value)
    if rix - lix != 0:
        return 1
    else:
        return 0


dic.sort()

for i in range(m):
    print(find(dic, arr[i]), end=" ")
