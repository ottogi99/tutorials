"""
열의 개수와 항목이 좀 더 많은 데이터가 있는 엑셀 파일을 가지고 다양한 방법으로 피벗 테이블 구성하는 방법을 살펴봅니다.
"""
from pathlib import Path

import pandas as pd

folder = './data/ch07/pivot_data/'
excel_file = folder + '피벗_테이블_심화_데이터.xlsx'

df_product = pd.read_excel(excel_file, sheet_name='농수산물_판매현황_데이터')
print(df_product)

"""
pd.pivot_table(index=["구분"], values=["주문량"], aggfunc='sum', margins=False)
"""
df_product_pivot = df_product.pivot_table(index=["구분"], values=["주문량"], aggfunc='sum', margins=False)
print(df_product_pivot)

"""
df_product.pivot_table(index=["구분","주문품"], values=["주문량"], aggfunc='sum', margins=True)
"""
df_product_pivot = df_product.pivot_table(index=["구분", "주문품"], values=["주문량"], aggfunc='sum', margins=True)
print(df_product_pivot)

"""
df_product.pivot_table(index=["구분", "주문품"], values=["주문량"], columns=["마트"], aggfunc='sum', margins=True, fill_value=0)
"""
df_product_pivot = df_product.pivot_table(index=["구분", "주문품"], values=["주문량"], columns=["마트"], aggfunc='sum', margins=True, fill_value=0)
print(df_product_pivot)

"""
df_product.pivot_table(index=["구분", "주문품"], values=["주문량", "판매액"], columns=["마트"], aggfunc='sum', margins=True, fill_value=0)
"""
df_product_pivot = df_product.pivot_table(index=["구분", "주문품"], values=["주문량", "판매액"], columns=["마트"], aggfunc='sum', margins=True, fill_value=0)
print(df_product_pivot)

"""
df_product.pivot_table(index=["마트"], values=["주문량", "판매액"], columns=["구분", "주문품"], aggfunc='sum', margins=True, fill_value=0)
"""
df_product_pivot = df_product.pivot_table(index=["마트"], values=["주문량", "판매액"], columns=["구분", "주문품"], aggfunc='sum', margins=True, fill_value=0)
print(df_product_pivot)

folder = './data/ch07/pivot_data/'
excel_file = folder + '피벗_테이블_심화_데이터_집계_결과.xlsx'

df_product_pivot.to_excel(excel_file, sheet_name='pivot_table')

print("생성 파일:", excel_file)
