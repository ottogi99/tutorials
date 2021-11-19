import pandas as pd
import numpy as np
import xlwings as xw
from pathlib import Path

"""
함수명: add_sum
역할: 엑셀 파일을 입력하면 처리 후 지정한 출력 디렉터리에 엑셀 파일로 출력
입력인자: excel_file (엑셀 파일, 경로 포함), output_dir (출력 디렉터리)
"""
def add_sum(excel_file, output_dir):
    df = pd.read_excel(excel_file)
    df['합계'] = df.sum(axis=1)

    new_file_name = excel_file.stem + "_합계_제목_추가" + ".xlsx"
    output_excel_file = Path(output_dir + new_file_name)

    excel_writer = pd.ExcelWriter(output_excel_file, engine='xlsxwriter')
    workbook = excel_writer.book

    title_format = workbook.add_format({
        'bold': True,
        'font_size': 20,
        'align': 'center',
        'valign': 'vcenter'
    })

    df.to_excel(excel_writer, sheet_name='Sheet1', index=False, startrow=2)

    worksheet = excel_writer.sheets['Sheet1']
    title_string = "판매량 합계: {}".format(df['담당자'][0])
    worksheet.write('E1', title_string, title_format)

    excel_writer.save()

    return output_excel_file


"""
여러 엑셀 파일에 적용하기
"""
input_dir = Path('./data/ch07/sales_data/input/')
excel_files = input_dir.glob('상반기_제품_판매량_*')
output_dir = './data/ch07/sales_data/output/'

print("[출력 디렉터리", output_dir)

for excel_file in excel_files:
    output_excel_file = add_sum(excel_file, output_dir)
    print("[출력 파일]", output_excel_file.name)
