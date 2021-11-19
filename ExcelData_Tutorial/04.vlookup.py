import pandas as pd
import numpy as np
import xlwings as xw
from pathlib import Path

"""
함수명: add_sum
역할: 엑셀 파일을 입력하면 처리 후 지정한 출력 디렉터리에 엑셀 파일로 출력
입력인자: excel_file (엑셀 파일, 경로 포함), output_dir (출력 디렉터리)
"""

"""
원본 엑셀 파일 읽기
"""
folder = './data/ch07/func_data/'
excel_file = folder + '주문내역_샘플.xlsx'
df = pd.read_excel(excel_file)

"""
참조 엑셀 파일
"""
excel_file = folder + '주문내역_참조데이터.xlsx'
df_ref = pd.read_excel(excel_file)

"""
특정 열을 기준으로 두 개의 DataFrame 데이터를 가로 방향으로 병합하는 merge()를 이용해
DataFrame 데이터 df에 df_ref를 병합합니다.
"""
df_new = df.merge(df_ref, how='left', on='제품명')
# print(df_new)

"""
df_new에서 열의 순서를 변경
"""
df_new = df_new[['주문번호', '제품명', '제품코드', '제품가격', '수량', '발주처']]
# print(df_new)

"""
df_new를 엑셀 파일로 쓰기
"""
excel_file_new = folder + '주문내역_샘플_new.xlsx'
sheet_name1 = '참조 데이터 표 엑셀 파일 이용해서 데이터 입력'
df_new.to_excel(excel_file_new, sheet_name=sheet_name1, index=False)

print("생성한 엑셀 파일:", excel_file_new)
