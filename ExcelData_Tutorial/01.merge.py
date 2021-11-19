import pandas as pd
import numpy as np
import xlwings as xw
from pathlib import Path

input_folder = './data/ch07/sales_data/input'
raw_data_dir = Path(input_folder)
excel_files = raw_data_dir.glob('상반기_제품_판매량_*')

total_df = pd.DataFrame()
total_df2 = pd.DataFrame()

for excel_file in excel_files:
    df = pd.read_excel(excel_file)
    # 세로방향으로 연결, 순차적으로 index 증가
    total_df = total_df.append(df, ignore_index=True)

folder = './data/ch07/sales_data/'
merged_excel_file = folder + '상반기_제품_판매량_통합.xlsx'

total_df.to_excel(merged_excel_file,
                  sheet_name='상반기_제품_판매량_통합',
                  index=False)

print("생성 파일:", merged_excel_file)

# # 판다스의 read_excel()로 엑셀 파일을 열지 못하는 경우 (보안 등의 이유로)
# for excel_file in excel_files:
#     wb = xw.Book(excel_file)
#     sht = wb.sheets['Sheet1']
#
#     df = sht.range('A1').options(pd.DataFrame,
#                                  expand='table',
#                                  index=False).value
#
#     wb.close()
#
#     total_df2 = total_df2.append(df, ignore_index=True)
#
# print(total_df2)

month = ['1월', '2월', '3월', '4월', '5월', '6월']
total_df[month] = total_df[month].astype(np.int32)
print(total_df)
