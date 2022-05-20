T = int(input())
for test_case in range(1, T+1):
    money = int(input())
    paper = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    arr = [0 for _ in range(8)]
    print("#{}".format(test_case))
    for coin in paper:
        if coin <= money:
            print(money // coin, end = " ")
            money = money % coin
        else:
            print(0, end = " ")
    print()