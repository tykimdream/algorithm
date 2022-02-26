from unittest import result


n = int(input())
data = list(map(int, input().split()))
data.sort()

# 각 그룹의 인원수
members_in_group = 0
# 총 그룹의 수
total_group = 0

for i in data:
    members_in_group += 1
    if members_in_group >= i:
        total_group += 1
        members_in_group = 0

print(total_group)
