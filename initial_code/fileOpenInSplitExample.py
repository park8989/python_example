# with as 文でOpne Read or Writeしたファイルを自動で閉じる
with open("hello_world.txt", "r") as fileobj:
    text = fileobj.read()
    print(text)   


# テキストファイルの中の文字列の単語リストを作る
with open("hello_world.txt", "r") as fileobj:
    text = fileobj.read()
    wordlist = text.split(" ")                         #split メソッドで空白毎に区切ってリスト化する。
    print(wordlist) 

# テキストファイルの中の文字列を一行ずつ読み込む
with open("hello_world.txt", "r") as fileobj:
    text = fileobj.read()
    lineList = text.split("\n")                         #split メソッドで空白毎に区切ってリスト化する。
    print(lineList) 

import pprint
my_Data = "I have data\n that is money\n and gold"      #適当な文字列
my_List = my_Data.split('\n')                           #上記の文字列を\nで分割し、リストを作る
pprint.pprint(my_List)                                  # listの印刷をして変更されていることを確認
# ['I have data', ' that is money', ' and gold']
for i in my_List:                                       # for文をkey毎に順次回す
    for j in i.split(' '):                              # 核リストのvalueを分割する
        if j == 'money':                                #moneyと一致すれば
            print('True')
        elif j == 'gold':
            print('OK')
        else:
            print('False')
            
# https://wikidocs.net/13 
# 文字列説明、ハングル
# inを使い文章内の文字列を検索する
my_Data = "I have data\n that is money\n and gold"
my_List = my_Data.split('\n')　                       #上記の文字列を\nで分割し、リストを作る
ok_Data = []                                          #カラのリストを用意して、文字列を含んだらOK文字を格納する
for i in my_List:                                     # for文をkey毎に順次回す
    if 'money' in i:                                  # listの値にmoneyが入っていれば
        ok_Data.append('OK')                          # OKを追加する
    else:
        pass
if len(ok_Data) > 0:                                  # OKが入っていれば、OKを出す
    print('OK')
else:
    print('NG')

 
    
# openpyxlを使うためには、Terminal mode　でインストールしてから使う
# pip install openpyxl
# <xlsxファイルの特定のcellに値を追加する>
import openpyxl as px
wb = px.load_workbook("example.xlsx")
sheetName = wb.sheetnames[0]                          # ０は一番左側のシートを意味
sheet = wb[sheetname]
sheet["A1"].value = "OK"
wb.save("example.xlsx")

