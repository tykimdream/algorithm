# n, k = map(int, input().split())

# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# a.sort(reverse=True)
# b.sort(reverse=True)

# sum = 0
# for i in range(n-k):
#     sum += a[i]

# for i in range(k):
#     sum += b[i]

# print(sum)

# Sol
n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
print(sum(a))
