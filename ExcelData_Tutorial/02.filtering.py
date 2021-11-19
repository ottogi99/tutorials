import pandas as pd
import numpy as np
import xlwings as xw
from pathlib import Path

folder = './data/ch07/sales_data/'
excel_file = folder + '상반기_제품_판매량_통합.xlsx'

df = pd.read_excel(excel_file)

filtered_df = df[(df['제품명'] == '스마트폰') | (df['제품명'] == 'TV')]
print(filtered_df)

"""
Series의 isin() 메서드를 이용
"""
filtered_df = df[df['제품명'].isin(['스마트폰', 'TV'])]
print(filtered_df)




