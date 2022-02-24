# https://www.acmicpc.net/problem/11659
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
prefix = [0]

temp = 0

for i in range(n):
    temp += arr[i]
    prefix.append(temp)

for _ in range(m):
    start, end = map(int, input().split())
    print(prefix[end] - prefix[start-1])
