import pandas as pd
import numpy as np
import xlwings as xw
from pathlib import Path

"""
중간고사와 기말고사의 평균을 구하고 
평균을 이용해 학점을 구하는 예시
"""

folder = './data/ch07/condition_data/'
excel_file = folder + '시험성적.xlsx'
excel_file_new = folder + '시험성적_new.xlsx'
df = pd.read_excel(excel_file)

df['평균'] = df_mean = df[['중간고사', '기말고사']].mean(axis=1)     # 평균 계산
# print(df_mean)

# 평균에 따라서 학점 구분해 학점 열에 입력 (loc = line of condition?????)
df.loc[df_mean > 90, '학점'] = 'A'
df.loc[(df_mean >= 80) & (df_mean < 90), '학점'] = 'B'
df.loc[df_mean < 80, '학점'] = 'C'

sheet_name1 = "시험 성적 및 평가 결과"
df.to_excel(excel_file_new, sheet_name=sheet_name1, index=False)

print("생성한 엑셀 파일:", excel_file_new)
