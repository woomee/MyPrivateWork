#
# xlwingsを使ったバージョン
# ・test2.xlsmも問題無く読み込める
# 

import xlwings as xw
import sys

args = sys.argv

workbook = xw.Book(args[1])
print('load')

sheets = workbook.sheets
print(sheets)

for sheet in sheets:
    print(sheet.name)

    range = sheet.used_range

    print(range.rows.count)
    for row in range.rows:
        print(row.address, row.value)
   