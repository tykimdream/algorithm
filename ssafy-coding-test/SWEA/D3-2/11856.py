T = int(input())

for tc in range(1, T+1):
    string = input()
    dic = []
    result = []

    for i in string:
        if i not in dic:
            dic.append(i)
        result.append(i)

    _result = "Yes"
    for i in dic:
        if result.count(i) != 2:
            _result = "No"
    print("#{} {}".format(tc, _result))