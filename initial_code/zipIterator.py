#! python3
# 複数のリストを整列するzip関数

names = ['南', '安部', '朴']
ages = [24, 50, 18]
points = [100, 85, 90]

for i, j, k in zip(names, ages, points):
  print(i, j, k)
  
# 60干支を並べる（かんし）
# 10天干（てんかん）
# 12地支（ちし）
up = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
ups = up*6
down = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
downs = down*5
for i, j in zip(ups, downs):
    if i != '癸':
        print(i + j, end=", ")
    else:
        print(i + j)

#以下は表示結果
#甲子, 乙丑, 丙寅, 丁卯, 戊辰, 己巳, 庚午, 辛未, 壬申, 癸酉
#甲戌, 乙亥, 丙子, 丁丑, 戊寅, 己卯, 庚辰, 辛巳, 壬午, 癸未
#甲申, 乙酉, 丙戌, 丁亥, 戊子, 己丑, 庚寅, 辛卯, 壬辰, 癸巳
#甲午, 乙未, 丙申, 丁酉, 戊戌, 己亥, 庚子, 辛丑, 壬寅, 癸卯
#甲辰, 乙巳, 丙午, 丁未, 戊申, 己酉, 庚戌, 辛亥, 壬子, 癸丑
#甲寅, 乙卯, 丙辰, 丁巳, 戊午, 己未, 庚申, 辛酉, 壬戌, 癸亥


# 要素間の場合の数を表示する
import itertools
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
people = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L')
for person, number in itertools.product(people, numbers):
    if number != 10:
       print(person, number, end=', ')
    else:    
      print(person, number)
      
      
 
