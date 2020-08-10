import xlrd,xlwt
import os

wb = xlrd.open_workbook('11.xls')
sheet = wb.sheet_by_name('Sheet1')

colValue = sheet.col_values(0)
for rowvalue in colValue:
    print(rowvalue)
    print(os.path.dirname(rowvalue))

