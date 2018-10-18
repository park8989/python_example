#! python3
# https://news.mynavi.jp/article/zeropython-16/
# PythonからGoogleドライブを操作する
# Manipulating Google Drive from Python

# ライブラリ「PyDrive」をインストールする
$ pip install google-api-python-client PyDrive
# 以下のURLにアクセスして、プロジェクトを作成し、
# APIを利用する際に必要となる「OAuth クライアントID」と
#「クライアントシークレット」を発行してもらう。
# https://console.developers.google.com/[Google Developers Console]
# 上記URLにアクセスしたら、画面左側にある「ダッシュボード」をクリックしよう。
# すると、プロジェクトを作成するようにと、ダイアログが表示されるので、
# 適当なプロジェクト名を入力して、プロジェクトを作成する。

# 次に、画面左側にある「認証情報」をクリックしよう。
# そして、「認証情報を作成」のボタンを押して
# 「OAuth クライアント ID」をクリック。
# 次いで「その他」を選んで名前を入力して、
# 「作成」のボタンをクリックする。

# すると、「クライアント ID」と「クライアント シークレット」の二つの情報が得られるので、
# これをコピーしてメモっておこう。これは、後ほどプログラムの中で利用する。
