"""
엑셀에서 조건부 서식 적용으로 셀이 특정 조건을 만족하는지를 검사해 셀 서식을 다르게 지정할 수 있습니다.
"""

import pandas as pd
import numpy as np
import xlwings as xw
from pathlib import Path


folder = './data/ch07/condition_data/'
excel_file = folder + '시험성적_new.xlsx'
excel_file_new2 = folder + '시험성적_new2.xlsx'
df = pd.read_excel(excel_file)

excel_writer = pd.ExcelWriter(excel_file_new2, engine='xlsxwriter')

sheet_name1 = '조건부서식'
df.to_excel(excel_writer, sheet_name=sheet_name1, index=False)

workbook = excel_writer.book
worksheet = excel_writer.sheets[sheet_name1]

cell_format = workbook.add_format()
cell_format.set_bg_color('yellow')

# 조건부 서식 지정
worksheet.conditional_format(1, 3, 10, 3,   # 시작_행_번호, 시작_열_번호, 끝_행_번호, 끝_열_번호
{'type': 'cell',                            # 지정된 범위의 셀이
 'criteria': '>=',                          # value 이상 이면
 'value': 90,
 'format': cell_format})                    # cell_format 서식 적용

# worksheet.conditional_format('D2:D11',      # 시작_셀_주소:끝_셀_주소
# {'type': 'cell',                            # 지정된 범위의 셀이
#  'criteria': '>=',                          # value 이상 이면
#  'value': 90,
#  'format': cell_format})                    # cell_format 서식 적용

excel_writer.save()

print("생성한 엑셀 파일:", excel_file_new2)
