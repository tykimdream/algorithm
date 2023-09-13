arr = [True for _ in range(1000001)] 

for i in range(2, 1001):
    if arr[i]:
        for k in range(i + i, 1000001, i):
            arr[k] = False

while True:
    n = int(input())
    if n == 0:
        break

    for i in range(3, len(arr)):
        if arr[i] and arr[n - i]:
            print(n, "=", i, "+", n-i)
            break