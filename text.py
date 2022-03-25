# arr = [1, 1, 2, 2, 3, 4, 5, 6, 8]

# print(arr)
# print()
# print(arr.index(1))
# print(arr.count(1))

# num = "01022322222"
# x = len(num) - 4
# print(num[x:])


# phone_number = "01033334444"
# answer = ''
# temp = []
# leng = len(phone_number) - 4

# for i in range(leng):
#     temp.append('*')

# print(temp)

# for i in range(leng):
#     answer = ''.join(temp)

# x = len(phone_number) - 4
# number = phone_number[x:]
# print(answer+number)


# answer.append(number)

# numbers = [2, 1, 3, 4, 1]
# numbers = [5, 0, 2, 7]

# numbers.sort()
# print(numbers)
# result = []
# n = len(numbers)
# for i in range(n):
#     for j in range(i+1, n):
#         result.append(numbers[i]+numbers[j])

# print(list(set(result)))
# answer = []
# temp = set(result)

# for i in range(n):
#     answer.append(temp[i])

# print(answer)

# for i in range(2, 4):
#     print(i)

# print(1.618 ** 4)


t = int(input())

for _ in range(t):
    n = int(input())
    if n == 0:
        print(1, 0)
        continue
    dp_0 = [0] * (n+1)
    dp_1 = [0] * (n+1)
    dp_0[0] = 1
    dp_1[1] = 1

    for i in range(2, n+1):
        dp_0[i] = dp_0[i-1] + dp_0[i-2]
        dp_1[i] = dp_1[i-1] + dp_1[i-2]
    print(dp_0[n], dp_1[n])
