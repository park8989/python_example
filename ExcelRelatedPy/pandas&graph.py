
import pandas as pd
# Excel/CSVのライブラリpandasを取り込み、pdという名前に定義

import matplotlib.pyplot as plt
# グラフ化のライブラリmatplotlibの中のpyplotという部分を取り込んで、pltという名前にする。

d = pd.read_csv('test.csv')
# pandasで提供されているCSV読み込み関数を実行し、その結果をdという変数に格納する。
plt.plot(d)
# グラフを描く関数を実行する
plt.show()
# 結果をポップアップウィンドウで表示する。
