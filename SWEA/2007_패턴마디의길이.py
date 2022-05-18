# n = int(input())
#
# for delta in range(n):
#     arr = input()
#     x = len(arr)
#     target = "efqwewfqnjkqefwljbkqefwbjlkqefwlbjk"
#     for i in range(x):
#         for j in range(i+1, x):
#             if arr[j] == arr[i]:
#                 flag = 0
#                 for k in range(j - i - 1):
#                     if j + k < x and arr[j+k] != arr[i+k]:
#                         flag = 1
#                         break
#                 if flag == 0:
#                     target = arr[i:j]
#                     break
#                 else:
#                     continue
#     print("#{} {}".format(delta+1, arr.count(target)))

n = int(input())

for delta in range(n):
    arr = input()
    x = len(arr)
    target = 0

    for i in range(x):
        for j in range(i+1, x):
            if arr[j] == arr[i]:
                flag = 0
                for k in range(j - i + 1):
                    if j + k < x and arr[j+k] != arr[i+k]:
                        flag = 1
                        break
                if flag == 0:
                    target = j - i
                    break
            if target > 0:
                break
    print("#{} {}".format(delta+1, target))

