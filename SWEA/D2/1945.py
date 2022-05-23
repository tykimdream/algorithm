T = int(input())

for tc in range(1, T+1):
    n = int(input())
    prime = [2, 3, 5, 7, 11]
    prime_count = [0, 0, 0, 0, 0]
    for i in range(5):
        while n % prime[i] == 0:
            prime_count[i] += 1
            n //= prime[i]
    print("#{}".format(tc), end = ' ')
    print(*prime_count)