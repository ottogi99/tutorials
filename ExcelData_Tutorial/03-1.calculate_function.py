import pandas as pd
import numpy as np
import xlwings as xw
from pathlib import Path


def product_sum(df_prod, product_name):
    df_prod['상반기합계'] = df_prod.sum(axis=1)
    df_prod_filter = df_prod[df_prod['제품명'] == product_name]
    df_prod_filter_sum = df_prod_filter.sum()

    df_prod_filter_sum['제품명'] = product_name
    df_prod_filter_sum['담당자'] = '전체'
    df_prod_filter_sum['지역'] = '전체'

    df_prod_filter_sum_total = df_prod_filter.append(df_prod_filter_sum, ignore_index=True)

    return df_prod_filter_sum_total


folder = './data/ch07/sales_data/'
excel_file = folder + '상반기_제품_판매량_통합.xlsx'

df_prod = pd.read_excel(excel_file)

excel_file_out = folder + '상반기_제품별_판매량_합계.xlsx'

excel_writer = pd.ExcelWriter(excel_file_out, engine='xlsxwriter')

workbook = excel_writer.book

title_format = workbook.add_format({
    'bold': True,
    'font_size': 20,
    'align': 'center',
    'valign': 'vcenter'
})

product_names = ["스마트폰", "TV", "냉장고"]

for product_name in product_names:
    df_prod_sum = product_sum(df_prod, product_name)
    # print(df_prod_sum)
    df_prod_sum.to_excel(excel_writer,
                         sheet_name=product_name,
                         index=False,
                         startrow=2)

    worksheet = excel_writer.sheets[product_name]
    title_string = "상반기 판매량 합계: {}".format(product_name)
    worksheet.write('E1', title_string, title_format)

excel_writer.save()

print("출력 엑셀 파일:", excel_file_out)


