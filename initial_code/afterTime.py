#! python3
#timedeltaを使って二日後、二時間後、20分後の時間を表示する。

import datetime

now = datetime.datetime.now() # 今の時間
tomorrow_this_time = datetime.timedelta(days=2) #二日後の時間
print(now+tomorrow_this_time)

after_hours_time = datetime.timedelta(hours=2) # 二時間後の時間
print(now+after_hours_time)

after_minutes_time = datetime.timedelta(minutes=20) # 20分後の時間
print(now+after_minutes_time)

