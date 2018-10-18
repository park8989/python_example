#! python3
# 形態素解析を行うライブラリ「Janome」
# Janomeのインストール

pip install janome

                                                                   # Janomeを使うための宣言 --- (*1)
from janome.tokenizer import Tokenizer
tok = Tokenizer()                                                  # Janomeの準備 --- (*2)
tokens = tok.tokenize("今日は家族でラーメンを食べに行った。")
                                                                   # 形態素に分割 --- (*3)
for t in tokens:                                                   # 分割結果を確認 --- (*4)
   print(t)
