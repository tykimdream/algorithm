# left, right = map(int, input("왼쪽 오른쪽 인덱스 값을 입력하시오 : ").split())

# arr = [10, 20, 30, 40, 50]
# n = len(arr)
# prefix = [0] * (n + 1)

# for i in range(1, n+1):
#     prefix[i] = arr[i-1] + prefix[i-1]

# print(prefix)
# print(prefix[right] - prefix[left-1])

# 부드러운 버젼
left, right = map(int, input("왼쪽 오른쪽 인덱스 값을 입력하시오 : ").split())

arr = [10, 20, 30, 40, 50]
prefix = [0]
sum_value = 0

for i in arr:
    sum_value += i
    prefix.append(sum_value)

print(prefix[right] - prefix[left-1])
