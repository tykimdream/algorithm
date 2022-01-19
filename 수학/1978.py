# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# a = int(input())
# numbers = list(map(int, input().split()))

# count = 0

# for i in range(0, a):
#     flag = 0

#     for j in range(2, numbers[i]):
#         if numbers[i] == 1:
#             continue
#         if(numbers[i] % j == 0):
#             # 소수가 아닌 경우
#             flag += 1
#             break
#     if(flag == 0):
#         count += 1

# print(count)

# a = int(input())
# count = 0

# for i in range(2, a):
#     if(a % i == 0):
#         print('소수가 아닙니다.')
#         count+1

# if(count == 0):
#     print('소수입니다.')

a = int(input())
numbers = list(map(int, input().split()))
count = 0

for i in numbers:
    flag = 0
    if(i == 1):
        continue
    for j in range(2, i+1):
        if(i % j == 0):
            # 소수가 아닌 경우
            flag += 1
    if(flag == 1):
        count += 1

print(count)
