#! python3
# Python's comprehension notation

print([i for i in range(0, 100)])    　　                             # 0-99をリスト化

list_3 = [i for i in range(0, 100)]				      # 0-99のリストを変数 list_3に渡す。
print(list_3)

print([0 for i in range(0, 100)])   　　                              # 0を100個リスト化
print([i % 2 for i in range(0, 100)])                                 # 0,1,0,1 が繰り返される

print([i for i in range(0, 100) if i % 3 == 0])
x3 = []                                                               # 3の倍数
x3.extend([i for i in range(0, 100) if i % 3 == 0])
print(x3, len(x3))

x3 = [i for i in range(0, 100) if i % 3 == 0]			      #　上の結果と同じ
print(x3, len(x3))

import os, glob, time

[f for f in glob.glob("*") if os.stat(f).st_mtime > time.time() - 60*60*24 ]
					　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　#time.time()で現在時刻をエポック秒で取得する。
					　　　　　　　　　　　　　　#glob.glob("*")でカレントディレクトリのファイルの一覧を列挙


# 入れ子構造にすることも可能
print([(x, y) for x in range(3) for y in range(3)])
#[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

listx = [1, 2, 3]
listy = ['a', 'b', 'c']
listxy = [(x, y) for x in listx for y in listy]
print(listxy)

# 九九の表を作る
print([(x * y) for x in range(1, 10) for y in range(1, 10)])
# [1, 2, 3, 4, 5,~~~~~ 54, 63, 72, 81]

print([str(x) + '*' + str(y) + '=' +  str(x * y) for x in range(1, 10) for y in range(1, 10)])
#['1*1=1', '1*2=2',,,,,,'9*8=72', '9*9=81']

kuku = [(x,y,x*y) for x in range(1, 10) for y in range(1,10)]
st = ''
for x,y,z in kuku:
    st += '{}*{}={} '.format(x,y,z)
    if y == 9: 
	st += "\n"　　　　　　　　　　　　　　　　　　　　　　　　# 9で改行する
print(st)


