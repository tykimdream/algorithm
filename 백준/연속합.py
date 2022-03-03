# n = int(input())
# arr = list(map(int, input().split()))

# dp = [0] * (n)
# for i in range(n-1):
#     dp[i] = max(arr[i] + arr[i+1], arr[i])


# if max(dp) < max(arr):
#     max = max(arr)
# else:
#     max = max(dp)

# print(max)

n = int(input())
a = list(map(int, input().split()))
sum = []
sum.append(a[0])
for i in range(n - 1):
    sum.append(max(sum[i] + a[i + 1], a[i + 1]))
print(max(sum))
