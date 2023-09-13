# n = int(input())

# # A B BA BAB BABBA BABBABAB BABBABABBABBA

# dp_a = [0] * (n+1)
# dp_a[2] = 1
# dp_a[3] = 1

# dp_b = [0] * (n+1)
# dp_b[0] = 1
# dp_b[1] = 1

# for i in range(2, n+1):
#     dp_b[i] = dp_b[i-1] + dp_b[i-2]

# for i in range(2, n+1):
#     dp_a[i] = dp_a[i-1] + dp_a[i-2]


# b = dp_b[n]
# a = dp_a[n]
# print(a, b)

# 다른사람의 코드
# k = int(input())

# a = [1, 0]
# b = [0, 1]

# for i in range(2, k+1):
#     a_num = a[i-1] + a[i-2]
#     a.append(a_num)
#     b_num = b[i-1] + b[i-2]
#     b.append(b_num)

# print(a[k], b[k])
n = int(input())

a = [1, 0]
b = [0, 1]

for i in range(2, n+1):
    a.append(a[i-1]+a[i-2])
    b.append(b[i-1] + b[i-2])

print(a[n], b[n])
