# https://www.acmicpc.net/problem/1654

k, n = map(int, input().split())

wire = []

for _ in range(k):
    wire.append(int(input()))

start = 1
end = max(wire)

# 최소 길이는 구해지지만 최대 값이 구해지지 않는다
# ex) 188cm에서 같은 값이 구해지지만 200cm가 최대 값이다.
# while True:
#     piece = 0
#     mid = (start+end) // 2
#     for i in range(k):
#         piece += wire[i] // mid
#     if piece == n:
#         print(mid)
#         break
#     elif piece < n:
#         end = mid-1
#     elif piece > n:
#         start = mid+1

# Sol 1
while start <= end:
    piece = 0
    mid = (start + end) // 2
    for cutted in wire:
        piece += cutted // mid
    if piece >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)
