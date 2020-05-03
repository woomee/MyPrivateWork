#
# xlwingsを使ったバージョン
# ・test2.xlsmも問題無く読み込める
# ・試しにtest2.xlsmに書き込み
#     ⇒OK!

import xlwings as xw
import sys

args = sys.argv

workbook = xw.Book('../../../data/test2.xlsm')
print('load')

sheet = workbook.sheets['見積明細書入力(請負準委任)']

sheet.range('H25').value='テスト'

workbook.save('../../../data/test2s.xlsm')

