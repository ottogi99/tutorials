"""
웹 사이트의 다양한 정보 중에서 표(table) 형식으로 정리된 데이터는 비교적 간단한 방법으로 추출할 수 있습니다.
웹 사이트에 있는 표 데이터를 파이썬을 이용해 추출한 후 가공해서 엑셀로 저장하는 방법을 살펴봅니다.
"""
from pathlib import Path

import pandas as pd

"""
dfs = pd.read_html(url[, header = row_num][, options])
read_html()은 반환값은 dataFrame의 list임.
"""
url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%ED%99%98%EC%9C%A8'

dfs = pd.read_html(url)

# replace는 dataFrame의 함수임. dfs[0]은 dataFrame임.
exchange_rate_df = dfs[0].replace({'전일대비상승': '▲', '전일대비하락': '▼'}, regex=True)
print(exchange_rate_df)

# folder = './data/ch07/webpage_data/'
# excel_file = folder + '네이버_환율_검색_결과_표_데이터.xlsx'
#
# exchange_rate_df.to_excel(excel_file, index=False)
# print("생성 파일:", excel_file)


"""
네이버 금율 환율 정보 사이트를 이용
"""
# url = 'https://finance.naver.com/marketindex/?tabSel=exchange#tab_section'
url = 'https://finance.naver.com/marketindex/exchangeList.nhn'

dfs = pd.read_html(url, header=1)
# head()를 이용해 전체 데이터 중 앞의 일부만 표시 (9행(0~8)만 표시)
print(dfs[0].head(9))

folder = './data/ch07/webpage_data/'
excel_file = folder + '네이버_금융_환율_리스트.xlsx'

dfs[0].to_excel(excel_file, index=False)
print("생성 파일:", excel_file)



