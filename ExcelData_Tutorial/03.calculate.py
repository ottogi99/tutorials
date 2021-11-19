import pandas as pd
import numpy as np
import xlwings as xw
from pathlib import Path

folder = './data/ch07/sales_data/'
excel_file = folder + '상반기_제품_판매량_통합.xlsx'

df = pd.read_excel(excel_file)

"""
행별 합계 구하기
DataFrame_data.sum([axis=0 or 1])
axis=0은 세로방향으로 합, axis=1 가로방향으로 합
"""
df_sum = df.sum(axis=1)
df['상반기합계'] = df_sum

print(df)
"""
열별 합계 구하기
"""
df_filter = df[df['제품명'] == '스마트폰']
df_filter_sum = df_filter.sum()
df_filter_sum['제품명'] = '스마트폰'
df_filter_sum['담당자'] = '전체'
df_filter_sum['지역'] = '전체'
df_filter_sum_total = df_filter.append(df_filter_sum, ignore_index=True)
print(df_filter)
print(df_filter_sum_total)

