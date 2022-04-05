# https://www.acmicpc.net/problem/11723

t = int(input())

bit = 0

for _ in range(t):
    command = input().split()

    # 뒤에 숫자 없는 커맨드부터 처리하자
    if command[0] == 'all':
        bit = (1 << 20)-1
    elif command[0] == 'empty':
        bit = 0
    else:
        oper = command[0]
        num = int(command[1]) - 1

        if oper == 'add':
            bit |= (1 << num)
        elif oper == 'remove':
            bit &= ~(1 << num)
        elif oper == 'check':
            if bit & (1 << num) == 0:
                print(0)
            else:
                print(1)
        elif oper == 'toggle':
            bit = bit ^ (1 << num)
