T = int(input())
result = []
for _ in range(1, T+1):
    a, b, c, d = map(int, input().split())
    alice = a/b
    bob = c/d
    if alice == bob:
        result.append("DRAW")
    elif alice > bob:
        result.append("ALICE")
    else:
        result.append("BOB")

for tc in range(T):
    print("#{} {}".format(tc + 1, result[tc]))
