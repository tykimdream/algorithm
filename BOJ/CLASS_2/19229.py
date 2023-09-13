def is_prime(n):
    if n < 2:
        return False
    temp = int(n ** 0.5) + 1
    for t in range(2, temp):
        if n % t == 0:
            return False
    return True


n, m = map(int, input().split())
for i in range(n, m + 1):
    if is_prime(i):
        print(i)
