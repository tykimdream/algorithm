from itertools import combinations

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    comb = list(combinations(arr, 3))

    result = []
    for i in range(len(comb)):
        result.append(sum(comb[i]))
    # print(list(set(result)).sort())
    pro = sorted(list(set(result)))
    print("#{} {}".format(tc, pro[-5]))
