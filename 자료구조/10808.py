# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각 알파벳이 단어에 몇 개가 포함되어 있는지 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

word = input().rstrip()

count = [0]*26

for i in word:
    a = ord(i)-97
    count[a] += 1

for i in count:
    print(i, end=' ')
