# 22.02.04 11656
#  접미사 배열은 문자열 S의 모든 접미사를 사전순으로 정렬해 놓은 배열이다.

# baekjoon의 접미사는 baekjoon, aekjoon, ekjoon, kjoon, joon, oon, on, n 으로 총 8가지가 있고,
# 이를 사전순으로 정렬하면, aekjoon, baekjoon, ekjoon, joon, kjoon, n, on, oon이 된다.

# 문자열 S가 주어졌을 때, 모든 접미사를 사전순으로 정렬한 다음 출력하는 프로그램을 작성하시오.

from collections import deque
import sys
input = sys.stdin.readline

q = deque(input().rstrip())
ans = []

# print('current q : ', q, "current ans : ", ans)
# deque()의 popleft를 사용하여 왼쪽부터 하나씩 삭제해 가며 완성
for i in range(len(q)):
    if i == 0:
        will = list(q)
        ans.append(will)
    else:
        q.popleft()
        will = list(q)
        ans.append(will)

# 출력문, list에 가공한 값들을 저장한 뒤 출력한다.
# 전처리
list = []
for i in range(len(ans)):
    list.append(''.join(ans[i]))
list.sort()

# 출력
for i in list:
    print(i)
