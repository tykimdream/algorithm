T = int(input())

for i in range(T):
    n = int(input())
    zero = [1, 0, 1]
    one = [0, 1, 1]
    for i in range(3, n+1):
        zero.append((zero[i-1] + zero[i-2]))
        one.append((one[i-1]+one[i-2]))
    print(zero[n], one[n])
