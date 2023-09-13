T = int(input())
def HC(arr):
    for i in range(9):
        dic = list(range(1, 10))
        count = 0
        for j in range(9):
            if arr[i][j] in dic:
                count+=1
                dic.remove(arr[i][j])
        if count != 9:
            return False
    return True

def VC(arr):
    for i in range(9):
        dic = list(range(1, 10))
        count = 0
        for j in range(9):
            if arr[j][i] in dic:
                count+=1
                dic.remove(arr[j][i])
        if count != 9:
            return False
    return True

def BC(arr):
    for x in range(0, 7, 3):
        for y in range(0, 7, 3):
            dic = list(range(1, 10))
            count = 0
            for i in range(3):
                for j in range(3):
                    if arr[x + i][y + j] in dic:
                        dic.remove(arr[x+i][y+j])
                        count+=1
            if count != 9:
                return False
    return True

for test_case in range(1, T+1):
    sud = []
    result = 0
    for _ in range(9):
        sud.append(list(map(int, input().split())))
    if VC(sud) and HC(sud) and BC(sud):
        result = 1

    print("#{} {}".format(test_case, result))
