# initial_num = 1000000000
#
# thousand_sep = (format(initial_num, ',d'))
#
# print("Number before inserting commas : " + str(initial_num))
# print("Number after inserting commas: ", thousand_sep)

# arr = list(map(int, input().split()))
#
# print(arr)


# for i in range(2+1):
#     print(i)

n = int(input())
print()
arr = []
for _ in range(n):
    data = input().split()
    arr.append((data[0], int(data[1])))

array = sorted(arr, key=lambda student: student[1])

for x in array:
    print(x[0], end = ' ')