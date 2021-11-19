"""
워크시트에 있는 표 데이터를 파이썬의 자료형으로 읽는 방법

list_data = sht.range(cell_address).options(expand='table').value
array_data = sht.range(cell_address).options(np.array, expand='table').value
series_data = sht.range(cell_address).options(pd.Series, expand='table').value
df_data = sht.range(cell_address).options(pd.DataFrame, expand='table').value
"""
from pathlib import Path

import xlwings as xw
import numpy as np
import pandas as pd

folder = './data/ch06/'
excel_file = folder + 'xlwings_test_02.xlsx'

wb = xw.Book(excel_file)
sht = wb.sheets['Sheet1']

# 워크시트에 있는 표 데이터를 리스트 데이터로 읽기
list_data1 = sht.range('A2').options(expand='table').value
print(list_data1)

# 워크시트에 있는 표 데이터를 넘파이 배열 데이터로 읽기
array_data1 = sht.range('A7').options(np.array, expand='table').value
print(array_data1)

# 표 데이터를 판다스 Series 데이터로 읽기
series_data1 = sht.range('A10').options(pd.Series, expand='table', header=False).value
print(series_data1)

# 워크시트에 있는 표 데이터를 판다스의 Series 데이터로 읽기 (정수 index)
series_data2 = sht.range('B10').options(pd.Series, expand='table', header=False, index=False).value
print(series_data2)

# 워크시트에 있는 표 데이터를 판다스의 DataFrame 데이터로 읽기
df_data1 = sht.range('B17').options(pd.DataFrame, expand='table', index=False).value
print(df_data1)

"""
열별로 다른 형식의 데이터 있는 엑셀 워크시트 표 데이터를 판다스의 DataFrame 데이터로 읽는 경우
"""
folder = './data/ch06/'
excel_file = folder + 'xlwings_test_03.xlsx'

wb = xw.Book(excel_file)
sht = wb.sheets['Sheet1']

df_data3 = sht.range((1,1)).options(pd.DataFrame, expand='table', index=False).value
print(df_data3)

df_data3['사번'] = df_data3['사번'].astype(int) # 열 데이터의 자료형을 정수로 변환
print(df_data3)

wb.close()

"""
엑셀 파일을 프린터로 출력하기
xlwings <-> pywin32 <-> Win32 API <-> Excel

wb.sheets[sheet_name].api.PrintOut()
wb.api.PrintOut()
"""
# folder = './data/ch06/'   # 상대경로 설정시 pdf 파일로 저장하는 경우 오류가 발생한다.
folder = 'c:/repo/python/tutorials/xlxlibrary/data/ch06/'
excel_file = folder + 'xlwings_test_02.xlsx'
pdf_file = folder + 'xlwings_test_02.pdf'

wb = xw.Book(excel_file)
# wb.sheets['Sheet1'].api.PrintOut()
# wb.api.PrintOut()

"""
엑셀 파일을 PDF 파일로 출력하기
wb.sheets[sheet_name].api.ExportAsFixedFormat(0, pdf_file)
"""
file_path = Path(pdf_file)

if file_path.exists():
    file_path.unlink()

wb.sheets['Sheet1'].api.ExportAsFixedFormat(0, pdf_file)
# wb.api.ExportAsFixedFormat(0, pdf_file)

wb.close()

print("생성한 PDF 파일:", pdf_file)


