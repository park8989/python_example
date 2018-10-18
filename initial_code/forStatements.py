for element in ['月', '火', '水', '木', '金', '土', '日']:                     #リストのfor文
    print(element, end=" ")                                                   #printの時、改行せず、スペース開けて表示

week_day = ['月', '火', '水', '木', '金', '土', '日']                          #リストとして定義
for i in week_day:
    print(i, end=" ")
    
for i in range(len(week_day)):                                                 # リストのインテクス数でfor文で
    print(i, end=" ")                                                          # 0 1 2 3 4 5 6を表示
    print(week_day[i], end=" ")                                                # リストvalueを表示
    
week_day2 = list(enumerate(week_day))                                          # enumerateはリストとvalueを一緒に表示する
print(week_day2)                                                               # [(0, '月'), (1, '火'), (2, '水'), (3, '木'), (4, '金'), (5, '土'), (6, '日')]が表示される

for i, v in enumerate(week_day):
    print(i, v)                                                                # index valueが並んで表示される。
    print('{}:{}'.format(i,v))                                                 # 0:月


print()
for element in ('月', '火', '水', '木', '金', '土', '日'):                      #tupleのfor文
   print(element, end=" ")                                                     #printの時、改行せず、スペース開けて表示
print()

for character in 'あいうえお':                                                  # 文字列for文
   print(character)
   
for i in range(10):                                                            # range()のfor文
   print(i, end=" ")
   
print()
