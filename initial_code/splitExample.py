import pprint
my_Data = "I have data\n that is money\n and gold" #適当な文字列
my_List = my_Data.split('\n') #上記の文字列を\nで分割し、リストを作る
pprint.pprint(my_List) # listの印刷をして変更されていることを確認
# ['I have data', ' that is money', ' and gold']
for i in my_List: # for文をkey毎に順次回す
    for j in i.split(' '): # 核リストのvalueを分割する
        if j == 'money':   #moneyと一致すれば
            print('True')
        elif j == 'gold':
            print('OK')
        else:
            print('False')
            
# https://wikidocs.net/13 
# 文字列説明、ハングル
