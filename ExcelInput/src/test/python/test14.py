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

    used_range = sheet.used_range

#    print('rows count=', range.rows.count, ' columns count=', range.columns.count)
#    print('rows count=%d columns count=%d' % (range.rows.count,  range.columns.count))
#    print('rows count={} columns count={}'.format(range.rows.count,  range.columns.count))
    print(f'rows count={used_range.rows.count} columns count={used_range.columns.count}')

    # for row in range.rows:
    #     for cell in row.value:
    #         print(cell)
    min_row = used_range.row
    max_row = used_range.last_cell.row
    min_col = used_range.column
    max_col = used_range.last_cell.column

    print(min_row, max_row, min_col, max_col)

    for row in range(min_row, max_row):
        for col in range(min_col, max_col):
            cell = sheet.range((row, col))
            # None 以外の値をアドレス付きで出力
            if (cell.value != None):
                print(cell.address, cell.value)


    
