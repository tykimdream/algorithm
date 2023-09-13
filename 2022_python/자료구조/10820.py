# 문자열 N개가 주어진다. 이때, 문자열에 포함되어 있는 소문자, 대문자, 숫자, 공백의 개수를 구하는 프로그램을 작성하시오.

# 각 문자열은 알파벳 소문자, 대문자, 숫자, 공백으로만 이루어져 있다.

# 입력 초과
# import sys
# input = sys.stdin.readline

# while True:
#     ans = [0] * 4
#     string = input().rstrip()
#     for i in string:
#         a = ord(i)
#         if a >= ord('a') and a <= ord('z'):
#             ans[0] += 1
#         if a >= ord('A') and a <= ord('Z'):
#             ans[1] += 1
#         if a >= 0 and a <= 9:
#             ans[2] += 1
#         if i.isspace():
#             ans[3] += 1
#     print(ans)

import sys
input = sys.stdin.readline

while True:
    l, u, d, s = 0, 0, 0, 0
    string = input().rstrip('\n')
    if not string:
        break
    for i in string:
        if i.islower():
            l += 1
        if i.isupper():
            u += 1
        if i.isdigit():
            d += 1
        if i.isspace():
            s += 1
    print(l, u, d, s)
