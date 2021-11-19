"""
XlsxWriter를 사용해 리스트나 딕셔너리 데이터와 판다스의 DataFrame 데이터를 엑셀로 출력하는 방법
"""

import xlsxwriter

folder = './data/ch06/'
excel_file = folder + 'XlsxWriter_list_data_01.xlsx'

workbook = xlsxwriter.Workbook(excel_file)
worksheet = workbook.add_worksheet()
list_num = [10, 20, 30, 40]
list_num2 = [50, 60, 70, 80]

for col_num, value in enumerate(list_num):
    worksheet.write(0, col_num+1, value)

for row_num, value in enumerate(list_num2):
    worksheet.write(row_num+1, 0, value)

workbook.close()
print("생성한 엑셀 파일:", excel_file)


""" 
write_row(), write_column() 함수
"""
folder = './data/ch06/'
excel_file = folder + 'XlsxWriter_list_data_03.xlsx'

workbook = xlsxwriter.Workbook(excel_file)
worksheet = workbook.add_worksheet()

list_num = [10, 20, 30, 40]
list_num2 = [50, 60, 70, 80]

worksheet.write_row(0, 1, list_num)
worksheet.write_column(1, 0, list_num)

workbook.close()
print("생성한 엑셀 파일:", excel_file)

""" 
딕셔너리 데이터를 엑셀에 쓰는 방법
"""
dict_data = {'제품ID': ['P101', 'P102', 'P103', 'P104'],
             '판매가격': [5000, 7000, 8000, 10000],
             '판매량': [50, 93, 70, 48]}

folder = './data/ch06/'
excel_file = folder + 'XlsxWriter_dict_data_01.xlsx'

workbook = xlsxwriter.Workbook(excel_file)
worksheet = workbook.add_worksheet()

list_keys = dict_data.keys()
list_values = dict_data.values()

worksheet.write_row(0, 0, list_keys)

for col, list_value in enumerate(list_values):
    worksheet.write_column(1, col, list_value)

workbook.close()
print("생성한 엑셀 파일:", excel_file)

""" 
판다스 DataFrame 데이터 쓰기

df.to_excel(excel_file[, 
                        index = True(or False), 
                        header = True(or False),
                        sheet_name = 'Sheet1'
                        startrow = 0
                        startcol = 0 ] [, options])
"""
import pandas as pd

folder = './data/ch06/'
csv_file = folder + 'korea_rain.csv'
excel_file = folder + 'XlsxWriter_DataFrame_data_01.xlsx'

df = pd.read_csv(csv_file)

# 쓰기 엔진과 엑셀 파일을 지정해 ExcelWriter 객체 생성(excel_writer)
excel_writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
df.to_excel(excel_writer, sheet_name='Sheet1', index=False)
excel_writer.save()

print("생성한 엑셀 파일:", excel_file)
