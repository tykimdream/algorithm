# 22.02.03-04 11655
# ROT13은 카이사르 암호의 일종으로 영어 알파벳을 13글자씩 밀어서 만든다.

# 예를 들어, "Baekjoon Online Judge"를 ROT13으로 암호화하면 "Onrxwbba Bayvar Whqtr"가 된다.
# ROT13으로 암호화한 내용을 원래 내용으로 바꾸려면 암호화한 문자열을 다시 ROT13하면 된다.
# 앞에서 암호화한 문자열 "Onrxwbba Bayvar Whqtr"에 다시 ROT13을 적용하면 "Baekjoon Online Judge"가 된다.

# ROT13은 알파벳 대문자와 소문자에만 적용할 수 있다. 알파벳이 아닌 글자는 원래 글자 그대로 남아 있어야 한다.
# 예를 들어, "One is 1"을 ROT13으로 암호화하면 "Bar vf 1"이 된다.

# 문자열이 주어졌을 때, "ROT13"으로 암호화한 다음 출력하는 프로그램을 작성하시오.

# 2번 실행시 원점으로 안돌아옴
# import sys
# input = sys.stdin.readline

# word = input()
# ans = ""
# for i in word:
#     if i.isupper() or i.islower():
#         if(ord(i)+13) > 122 or (ord(i)+13 > 90 and ord(i)+13 < 97):
#             # if (ord(i) >= ord('m') and ord(i) <= ord('z')) and (ord(i) >= ord('M') and ord(i) <= ord('Z')):
#             ROT = ord(i)-13
#         else:
#             ROT = ord(i)+13
#         ans += chr(ROT)
#     else:
#         ans += i
# print(ans)

import sys
input = sys.stdin.readline

# word = input()
# ans = ""
# for i in word:
#     if i.isupper() or i.islower():
#         if(ord(i)+13) > 122 or (ord(i)+13 > 90 and ord(i)+13 < 97):
#             # if (ord(i) >= ord('m') and ord(i) <= ord('z')) and (ord(i) >= ord('M') and ord(i) <= ord('Z')):
#             ROT = ord(i)-13
#         else:
#             ROT = ord(i)+13
#         ans += chr(ROT)
#     else:
#         ans += i

word = input()
ans = ""
for i in word:
    if i.isupper():
        i = ord(i)+13
        if(i > 90):
            i -= 26
        ans += chr(i)
    elif i.islower():
        i = ord(i)+13
        if(i > 122):
            i -= 26
        ans += chr(i)
    else:
        ans += i

print(ans)
