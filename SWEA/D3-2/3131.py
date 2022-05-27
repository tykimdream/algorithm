arr = [1] * 1000001

for i in range(2, 1000001):
    if arr[i] == 1:
        for j in range(i*2, 1000001, i):
            arr[j] = 0

for i in range(2, 1000001):
    if arr[i] == 1:
        print(i, end=' ')