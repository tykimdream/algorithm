N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

max1 = arr[-1]
max2 = arr[-2]

max1_freq = M // K
max2_freq = M - (max1_freq * K)

print(max1_freq * max1 * K + max2_freq * max2)