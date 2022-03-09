# https://www.acmicpc.net/problem/2748

n = int(input())

fib = [0, 1, 1]
for i in range(3, n+1):
    fib.append(fib[i-1] + fib[i-2])

print(fib[n])
