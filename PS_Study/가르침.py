# https://www.acmicpc.net/problem/1062
# Condition

# 1. 5개 이하로 배우면 읽는 것이 불가능
#     1. 남극언어의 모든 단어는 "anta"로 시작되고, "tica"로 끝난다. // start : a, c, i, t, n
# 2. 단어는 중복되지 않지만 한 단어 안에 소문자들의 중복은 가능
#     1. 단어는 영어 소문자로만 이루어져 있고, 길이가 8보다 크거나 같고, 15보다 작거나 같다. 모든 단어는 중복되지 않는다.

# Process

# 1. SET을 활용하여 unique 문자들로 가공
# 2. acitn을 제외한 문제가 몇개 등장했는지 확인 - dic 활용
# 3. 그 중 무엇을 배워야 가장 많은 단어를 읽을 수 있는지 확인.

n, k = map(int, input().split())
word = []
if k < 5:
    print(0)
    exit()
for _ in range(n):
    word.append(input())

start = ['a', 'c', 'n', 'i', 't']
pre = []
# 어처피 acnit를 배우지 못하면 남극어를 사용할 수 없기 때문에
# 기본 단어를 기본으로 셋팅
k = k - len(start)


# 전처리
for i in range(n):
    if word[i][0:4] == 'anta' and word[i][-1:-5:-1] == 'acit':
        pre.append(list(set(word[i][4:-4])))

for i in range(n):
    for j in start:
        if j in pre[i]:
            pre[i].remove(j)

print(pre)
count = [0] * n
k = 0

stand = pre[0]
print(stand)
for k in range(n):
    stand = pre[k]
    for word in pre:
        for i in range(len(word)):
            flag = 0
            if word[i] not in stand:
                print(word, "는 배우지 못한다.")
                flag = 1
                break
        if flag == 0:
            print(word, "는 배울 수 있다.")
            count[k] += 1
    print()

print(count)

# 한글자씩만 다른 경우 처리할 수가 없다.
# EX TC3
