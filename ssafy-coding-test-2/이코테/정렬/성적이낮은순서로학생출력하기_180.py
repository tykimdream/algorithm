n = int(input())
print()
arr = []
for _ in range(n):
    data = input().split()
    print(data[0], data[1])
    arr.append((data[0], int(data[1])))

array = sorted(arr, key=lambda student: student[1])

for x in array:
    print(x[0], end = ' ')