T = int(input())

for tc in range(1, T+1):
    card = str(input())
    size = len(card)
    # S D H C
    arr = [[0] * 13 for _ in range(4)]
    flag = 0
    print("#{}".format(tc), end=' ')
    for i in range(0, size, 3):
        if card[i] == 'S':
            arr[0][int(card[i+1] + card[i+2])] += 1
            if arr[0][(int(card[i+1] + card[i+2]))] == 2:
                print("ERROR")
                flag = 1
                break
        elif card[i] == 'D':
            arr[1][(int(card[i+1] + card[i+2]))] += 1
            if arr[1][(int(card[i+1] + card[i+2]))] == 2:
                print("ERROR")
                flag = 1
                break
        elif card[i] == 'H':
            arr[2][(int(card[i+1] + card[i+2]))] += 1
            if arr[2][(int(card[i+1] + card[i+2]))] == 2:
                print("ERROR")
                flag = 1
                break
        elif card[i] == 'C':
            arr[3][(int(card[i+1] + card[i+2]))] += 1
            if arr[3][(int(card[i+1] + card[i+2]))] == 2:
                print("ERROR")
                flag = 1
                break
    if flag == 0:
        for i in range(4):
            print(13 - arr[i].count(1), end=' ')
        print()