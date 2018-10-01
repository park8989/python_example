#! python3
# 日付表示方法を変える

import datetime

today1= datetime.date.today()
today2= "{0:%Y:%m:%d}".format(today1)
today3= "{0:%Y.%m.%d}".format(today1)
today4= "{0:%Y年%m月%d日}".format(today1)
today5= "{0:%Y년%m월%d일}".format(today1)

print(today1)
print(today2)
print(today3)
print(today4)
print(today5)

#曜日を付け加える
p = today1.weekday()
day_week = {0: '月', 1 : '火', 2: '水', 3: '木', 4: '金', 5: '土', 6: '日'} # pの変数が得られる数字と曜日を関連付ける
print(day_week[p]) #曜日を返す
today6= "{0:%Y年%m月%d日}({1})".format(today1, day_week[p])
print(today6)


