n = int(input())
arr = []
for i in range(n):
    w, h = map(int, input().split())
    arr.append([w, h, 0])


for i in range(n):
    for j in range(n):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            arr[i][2] += 1

for i in range(n):
    print(arr[i][2] + 1, end=" ")
