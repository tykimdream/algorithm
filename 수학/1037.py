# 양수 A가 N의 진짜 약수가 되려면, N이 A의 배수이고, A가 1과 N이 아니어야 한다.
# 어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램을 작성하시오.

from importlib.util import find_spec


size = int(input())
divisor = list(map(int, input().split()))

divisor.sort()
first_num = divisor[0]
last_num = divisor[-1]

print(first_num * last_num)

# sol : sort를 안할수도있다. max, min 함수 사용
# size = int(input())
# divisor = list(map(int, input().split()))
# first_num = min(divisor)
# last_num = max(divisor)
# print(first_num * last_num)
