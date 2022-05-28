T = int(input())

cal = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

for tc in range(1, T+1):
    today = input()

    result = 6 - (cal.index(today))
    if today == "SUN":
        result = 7

    print("#{} {}".format(tc, result))