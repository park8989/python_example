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
      
 # 要素間の場合の数をリスト化する
import itertools
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
people = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L')
dataList = []
for person, number in itertools.product(people, numbers):
  dataList.extend([person + str(number)])
  
print(dataList)

# Data構造にする

import itertools
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
people = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L')
dataList = []
for person, number in itertools.product(people, numbers):
    dataList.extend([person + str(number)])
i = range(1, 121)
d = {i: daL for i, daL in zip(i, dataList)}
print(d)

# 出力

{1: 'A1', 2: 'A2', 3: 'A3', 4: 'A4', 5: 'A5', 6: 'A6', 7: 'A7', 8: 'A8', 9: 'A9', 10: 'A10', 11: 'B1', 12: 'B2', 13: 'B3', 14: 'B4', 15: 'B5', 16: 'B6', 17: 'B7', 18: 'B8', 19: 'B9', 20: 'B10', 21: 'C1', 22: 'C2', 23: 'C3', 24: 'C4', 25: 'C5', 26: 'C6', 27: 'C7', 28: 'C8', 29: 'C9', 30: 'C10', 31: 'D1', 32: 'D2', 33: 'D3', 34: 'D4', 35: 'D5', 36: 'D6', 37: 'D7', 38: 'D8', 39: 'D9', 40: 'D10', 41: 'E1', 42: 'E2', 43: 'E3', 44: 'E4', 45: 'E5', 46: 'E6', 47: 'E7', 48: 'E8', 49: 'E9', 50: 'E10', 51: 'F1', 52: 'F2', 53: 'F3', 54: 'F4', 55: 'F5', 56: 'F6', 57: 'F7', 58: 'F8', 59: 'F9', 60: 'F10', 61: 'G1', 62: 'G2', 63: 'G3', 64: 'G4', 65: 'G5', 66: 'G6', 67: 'G7', 68: 'G8', 69: 'G9', 70: 'G10', 71: 'H1', 72: 'H2', 73: 'H3', 74: 'H4', 75: 'H5', 76: 'H6', 77: 'H7', 78: 'H8', 79: 'H9', 80: 'H10', 81: 'I1', 82: 'I2', 83: 'I3', 84: 'I4', 85: 'I5', 86: 'I6', 87: 'I7', 88: 'I8', 89: 'I9', 90: 'I10', 91: 'J1', 92: 'J2', 93: 'J3', 94: 'J4', 95: 'J5', 96: 'J6', 97: 'J7', 98: 'J8', 99: 'J9', 100: 'J10', 101: 'K1', 102: 'K2', 103: 'K3', 104: 'K4', 105: 'K5', 106: 'K6', 107: 'K7', 108: 'K8', 109: 'K9', 110: 'K10', 111: 'L1', 112: 'L2', 113: 'L3', 114: 'L4', 115: 'L5', 116: 'L6', 117: 'L7', 118: 'L8', 119: 'L9', 120: 'L10'}
 
