#! python3
#timedeltaを使って二日後、二時間後、20分後の時間を表示する。

import datetime

now = datetime.datetime.now()                                                         # 今の時間
tomorrow_this_time = datetime.timedelta(days=2)                                       #二日の日数　2 days, 0:00:00
print(now+tomorrow_this_time)

after_hours_time = datetime.timedelta(hours=2)                                        # 二時間の時間　2:00:00　
print(now+after_hours_time)

after_minutes_time = datetime.timedelta(minutes=20)                                   # 0:20:00
print(now+after_minutes_time)

import calendar
print(calendar.month(2018, 1))
# 以下が返される

January 2018
Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31

