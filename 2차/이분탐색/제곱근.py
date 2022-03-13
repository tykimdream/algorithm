# https://www.acmicpc.net/problem/13706
n = int(input())

start = 1
end = n

while True:
    mid = (end + start) // 2
    if mid ** 2 == n:
        print(mid)
        break

    if mid ** 2 > n:
        end = mid

    if mid ** 2 < n:
        start = mid
