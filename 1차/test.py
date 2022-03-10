from collections import deque

priorities = [2, 1, 3, 2]
# d = deque([(i, v) for i, v in enumerate(priorities)])

# print(max(d)[0])
# print(max(d)[1])
# print(max(d))
# print()
# print("d : ", d)
# print()

# print(d.popleft())

# d1 = deque([(v, i) for i, v in enumerate(priorities)])
# print(d1)

# for i in range(len(d1)):
#     d1[i][1] = 0

# print(d1)

# d2 = deque((priorities, 0))
# print(d2)


people = [70, 50, 80, 50]
limit = 2

answer = 0
people.sort()
current = 1
print(people)

while len(people):
    if current + people[0] <= limit:
        current += people[0]
        print(answer, "번째 배에", people[0], "kg 승객 탑승")
        people.pop(0)
    elif current + people[0] > limit and len(people) > 0:
        answer += 1
        current = 0
    else:
        break

answer += 1


print(answer)
