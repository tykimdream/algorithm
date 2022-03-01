# arr = [1, 2, 3, 2, 5]
# n = len(arr)
# target = 5

# end = 0
# inter_sum = 0
# result = 0

# for start in range(n):
#     while inter_sum < target and end < n:
#         inter_sum += arr[end]
#         end += 1
#     if inter_sum == target:
#         result += 1
#     inter_sum -= arr[start]

# print(result)

arr = [1, 2, 3, 2, 5]
n = len(arr)
target = 5

end = 0
inter_sum = 0
count = 0

for start in range(n):
    while inter_sum < target and end < n:
        inter_sum += arr[end]
        end += 1
    if inter_sum == target:
        count += 1
    inter_sum -= arr[start]

print(count)
