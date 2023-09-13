# 10773

k = int(input())
q = []
for _ in range(k):
    t = int(input())
    if t == 0:
        q.pop()
    else:
        q.append(t)

print(sum(q))


# k = int(input())
# result = 0
# for _ in range(k):
#     t = int(input())
#     if t != 0:
#         result+=t

# print(t)
