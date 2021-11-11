"""
Series 데이터나 DataFrame 데이터에서 특정 행이나 열을 지정해 없애려면 drop()을 이용합니다.
단, drop()은 결측치 검사 없이 지정한 행이나 열을 삭제하니 주의
"""
import pandas as pd
import numpy as np

s3 = pd.Series([10, 20, 30, 40, np.nan, 60])
print("pd.Series([10, 20, 30, 40, np.nan, 60])=\n{0}".format(s3))

print("\n- 데이터에서 행을 제거")
print("\n- s3.drop(index=0)=\n{0}".format(s3.drop(index=0)))
print("\n- s3.drop(index=[1,3,5])=\n{0}".format(s3.drop(index=[1, 3, 5])))

folder = './data/ch05/'
csv_file = folder + 'electric_products.csv'

df3 = pd.read_csv(csv_file, encoding='utf-8')
print("\n- pd.read_csv(csv_file, encoding='utf-8')=\n{0}".format(df3))
print("\n- df3.drop(index=[1,2])=\n{0}".format(df3.drop(index=[1,2])))
print("\n- df3.drop(columns=['M3','M4'])=\n{0}".format(df3.drop(columns=['M3','M4'])))
print("\n- df3.drop(index=[1,2], columns=['M3','M4'])=\n{0}".format(df3.drop(index=[1,2], columns=['M3','M4'])))

