T = int(input())
print()
for test_case in range(1, T+1):
    h1, m1, h2, m2 = map(int, input().split())
    h = h1+h2
    m = m1+m2
    adj = 0
    if m > 60:
        adj = m // 60
    result = h + adj
    if result == 12 or result == 24:
        result = 12
    else:
        result %= 12

    print("#{} {} {}".format(test_case, result, m%60))

# 처음 풀었을 때
# T = int(input())
# for test_case in range(1, T+1):
#     h1, m1, h2, m2 = map(int, input().split())
#     adj = 0
#     if m1 + m2 > 60:
#         adj = (m1 + m2) // 60
#     print("#{} {} {}".format(test_case, (h1 + h2 + adj) % 12, (m1 + m2) % 60))