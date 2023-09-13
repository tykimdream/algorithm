# import sys
# op = int(input())
# dic = []
#
# for _ in range(op):
#     name, action = sys.stdin.readline().rstrip().split()
#     if action == 'enter':
#         dic.append(name)
#     elif action == 'leave':
#         if name in dic:
#             dic.remove(name)
# dic.sort(reverse=True)
# for i in dic:
#     print(i)

import sys
op = int(input())
dic = {}

for _ in range(op):
    name, action = sys.stdin.readline().rstrip().split()
    if action == 'enter':
        dic[name] = '1'
    elif action == 'leave':
        del dic[name]

temp = sorted(dic, reverse=True)
for i in temp:
    print(i)