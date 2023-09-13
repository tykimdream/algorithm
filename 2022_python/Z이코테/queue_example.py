from collections import deque
from posixpath import split

q = deque()

q.append(2)
q.append(3)
q.append(4)
q.append(5)
q.append(6)
q.append(7)
q.popleft()

q = list(q)
# al = []
# for i in len(q):
#     al.append(' '.join(q[i]))
# print(al)
q.reverse()
print(q)

al = []
for i in q:
    al.append(i)

print(al)
