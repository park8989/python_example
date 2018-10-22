#! python3
# shutil <shell utilities> ファイルのコピー、移動、名前変更、削除するための関数

import os
import shutil

shutil.copy('C:\\spam.txt', 'C:\\dilicious')                        # src = C:\\spam.txt, dst = C:\\dilicious
# 結果：C:\\dilicious\\spam.txt

shutil.copy('C:\\spam.txt', 'C:\\dilicious\\spam2.txt')             # src = C:\\spam.txt, dst = C:\\dilicious\\spam2.txt
# 結果：C:\\dilicious\\spam2.txt

shutil.copytree('C:\\spam, 'C:\\spam_backup')                       # src = C:\\spamフォルダをまるごと、dst = spam_backupへコピー

####################

import shutil

shutil.move('C:\\spam.txt', 'C:\\dilicious')                        # src = C:\\spam.txt, dst = C:\\diliciousへ移動する

shutil.copy('C:\\spam.txt', 'C:\\dilicious\\spam2.txt')             # src = C:\\spam.txt, dst = C:\\dilicious\\spam2.txt, ファイル名を変更して移動


9.1.3


