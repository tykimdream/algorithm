# 재귀 함수는 내부적으로 스택 자료구조와 동일하다
# def recur(i):
#     if i == 10:
#         return
#     print(i, "번째 함수에서 ", i+1, "번째 함수를 호출합니다.")
#     recur(i+1)
#     print(i, '번째 재귀함수를 종료합니다.')


# recur(1)

def fac(n):
    if n <= 1:
        return 1
    return n * fac(n-1)


print(fac(5))
