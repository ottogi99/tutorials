"""
셀의 피벗 테이블은 위크시트의 데이터를 요약, 분석, 탐색하고 부분합을 계산하는데 유용합니다.
파이썬의 판다스에는 엑셀의 피벗 테이블과 기능이 유사한 함수가 있으므로 이를 이용하면 엑셀 데이터를 편리하게 요약할 수 있습니다.
"""
from pathlib import Path

import pandas as pd

folder = './data/ch07/pivot_data/'
excel_file = folder + '피벗_테이블_기본_데이터.xlsx'

df_coffee = pd.read_excel(excel_file, sheet_name='커피_판매현황_데이터')
# print(df)

"""
pd.pivot_table(DataFrame_data, values=None, index=None, columns=None, aggfunc='mean', margins=False)
or
DataFrame_data.pivot_table(values=None, index=None, columns=None, aggfunc='mean', margins=False)

# 메뉴별 주문개수의 합계를 알고 싶다면 index=['메뉴'], values=['주문개수'], aggfunc='sum'으로 지정
"""
df_coffee_pivot = df_coffee.pivot_table(index=['메뉴'], values=['주문개수'], aggfunc='sum')
# print(df_coffee_sum)

"""
전체의 합계를 알고 싶다면 margins=True 옵션 추가
"""
df_coffee_pivot = df_coffee.pivot_table(index=['메뉴'], values=['주문개수'], aggfunc=['sum', 'count'], margins=True)
print(df_coffee_pivot)

folder = './data/ch07/pivot_data/'
excel_file = folder + '피벗_테이블_기본_데이터_집계_결과.xlsx'

df_coffee_pivot.to_excel(excel_file, sheet_name='pivot_table')

print("생성 파일:", excel_file)
