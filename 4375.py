# 4375 실버3
# 2와 5로 나누어 떨어지지 않는 정수 n(1 ≤ n ≤ 10000)가 주어졌을 때, 1로만 이루어진 n의 배수를 찾는 프로그램을 작성하시오.

# 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있고, n이 주어진다.
# 1로 이루어진 n의 배수 중 가장 작은 수의 자리수를 출력한다.

# Test Case
# 3           3
# 7           6
# 9901        12


while True:
    try:
        n = int(input())
    except:
        break

    count = 1
    num = 0

    while True:
        num = num*10 + 1
        num %= n
        if(num == 0):
            print(count)
            break
        else:
            count += 1


# while True:
#     try:
#         n = int(input())
#     except:
#         break
#     num = 0
#     count = 1

#     while True:
#         num = num*10 + 1
#         num %= n
#         if(num == 0):
#             print(count)
#             break
#         else:
#             count += 1
