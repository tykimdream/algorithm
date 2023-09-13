T = int(input())
arr = []
for i in range(T):
    data = input()
    arr.append((len(data), data))

arr = list(set(arr))
arr.sort()
for i in range(len(arr)):
    print(arr[i][1])