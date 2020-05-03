# openpyxlを利用
#
# ・test2.xlsmは読み込むのに時間がとてもかかる
#    だいたい10分くらい掛かるので使えない
#

import openpyxl
import sys

args = sys.argv

workbook = openpyxl.load_workbook(args[1], keep_vba=True, read_only=False)
print('load')

sheets = workbook.sheetnames
print(sheets)
