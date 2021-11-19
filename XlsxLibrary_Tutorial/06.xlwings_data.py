"""
파이썬의 리스트 데이터, 넘파이 배열 데이터, 판다스의 Series나 DataFrame 데이터를
엑셀의 셀에 쓰는 방법과 반대로 엑셀 파일에 있는 셀 데이터를 파이썬의 자료형으로 읽기

파이썬의 데이터를 엑셀 워크시트에 쓰기
sht.range((row, col)).value = table_data
sht.range(cell_address).value = table_data
"""

import xlwings as xw
import numpy as np
import pandas as pd

wb = xw.Book()
sht = wb.sheets['Sheet1']

# 리스트 데이터 쓰기
sht.range('A1').value = "리스트 데이터 쓰기"
list_data_2d = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
sht.range((2,1)).value = list_data_2d

# 넘파이 배열 데이터 쓰기
sht.range('A6').value = "넘파이 배열 데이터 쓰기"
list_data_1d = [10, 20, 30, 40, 50, 60]
numpy_data = np.array(list_data_1d)
sht.range((7,1)).value = numpy_data
# numpy_data_2d = np.reshape(list_data_1d, (2,3))
# sht.range((8,1)).value = numpy_data_2d

# 판다스 Series 데이터 쓰기
sht.range('A9').value = "판다스 Series 데이터 쓰기"
series_data = pd.Series(list_data_1d)
sht.range('A10').value = series_data

# 판다스 DataFrame 데이터 쓰기
sht.range('A16').value = "판다스 DataFrame 데이터 쓰기"
df_data = pd.DataFrame(list_data_2d, columns=['A', 'B', 'C'])
sht.range('A17').value = df_data

folder = './data/ch06/'
excel_file = folder + 'xlwings_test_02.xlsx'

wb.save(excel_file)

print("생성한 엑셀 파일:", excel_file)

# wb.close()
