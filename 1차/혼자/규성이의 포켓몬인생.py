from datetime import datetime

current_Poke = 60694
date_start = datetime.strptime("20160714", "%Y%m%d")
print(date_start)
date_today = datetime.now()
diff_day = date_today - date_start
print(diff_day.days)

print("하루당 잡아야 하는 포켓몬 : ", int(current_Poke/diff_day.days))
