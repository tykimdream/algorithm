T = int(input())

dic = ['a', 'e', 'i', 'o', 'u']

for tc in range(1, T+1):
    word = str(input())
    temp = ''
    for i in word:
        if i not in dic:
            temp += i

    print("#{} {}".format(tc, temp))