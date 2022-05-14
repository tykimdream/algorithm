T = int(input())
for test_case in range(1, T + 1):
    source = list(map(int, input().split()))

# tc 3번 같은게 문제임
# 나머지는 그냥 멕스에서 빼는 식으로 하면 되는데
# 최대값이 중간에 나오고 2번째 최대값이 등장하는거 처리가 문제
# ex 1 1 3 1 2