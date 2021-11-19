"""
xlwings는 엑셀 프로그램이 설치돼 있어야 이용할 수 있지만
엑셀 파일이 열려 있는 상태에서 파이썬 코드를 작서앻 바로 엑셀 파일에 반영되는 것을 확인할 수 있습니다.

https://www.xlwings.org

import xlwings as xw
wb = xw.Book()
wb = xw.Book(excel_file)
sht = wb.sheets[sheet_name]
sht.range((row, col)).value = cell_data
sht.range(cell_address).value = cell_data
cell_data = sht.range((row, col)).value
cell_data = sht.range(cell_address).value
wb.save(excel_file)
wb.close()
"""

import xlwings as xw

wb = xw.Book()

sht = wb.sheets['Sheet1']

sht.range((1,1)).value = 100
sht.range((2,1)).value = 3.14
sht.range((3,1)).value = "안녕"
sht.range('C1').value = '데이터 1'
sht.range('C2').value = '데이터 2'
sht.range('C3').value = '데이터 3'
sht.range('C4').value = '합계'
sht.range('D1').value = 10
sht.range('D2').value = 20
sht.range('D3').value = 30
sht.range('D4').value = '=SUM(D1:D3)'

print(sht.range('A1').value)
print(sht.range('A2').value)
print(sht.range('A3').value)
print(sht.range((1,4)).value)
print(sht.range((2,4)).value)
print(sht.range((3,4)).value)

folder = './data/ch06/'
excel_file = folder + 'xlwings_test_01.xlsx'

wb.save(excel_file)

print("생성한 엑셀 파일:", excel_file)

wb.close()