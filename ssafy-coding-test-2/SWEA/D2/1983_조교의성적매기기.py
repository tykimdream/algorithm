T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    grade = []
    # N 명의 학생의 성적을 받는다.
    for index in range(N):
        grade.append(list(map(int, input().split())))
    result = []
    for final_grade in grade:
        result.append((final_grade[0] * 0.35) + (final_grade[1] * 0.45) + (final_grade[2] * 0.2))
    stand = result[K-1]
    result.sort(reverse = True)
    target_rank = result.index(stand) + 1
    ratio = target_rank / N
    tier = "Un"
    if 0.0 <= ratio <= 0.1:
        tier = "A+"
    elif 0.1 < ratio <= 0.2:
        tier = "A0"
    elif 0.2 < ratio <= 0.3:
        tier = "A-"
    elif 0.3 < ratio <= 0.4:
        tier = "B+"
    elif 0.4 < ratio <= 0.5:
        tier = "B0"
    elif 0.5 < ratio <= 0.6:
        tier = "B-"
    elif 0.6 < ratio <= 0.7:
        tier = "C+"
    elif 0.7 < ratio <= 0.8:
        tier = "C0"
    elif 0.8 < ratio <= 0.9:
        tier = "C-"
    elif 0.9 < ratio <= 1.0:
        tier = "D0"
    print("#{} {}".format(test_case, tier))
