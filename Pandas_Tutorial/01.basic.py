"""
데이터 구조와 생성
판다스의 데이터 구조(타입)에는 라벨이 있는 1차원 구조의 Series와
엑셀과 같은 표 형식의 데이터를 담을 수 있는 DataFrame이 있다.
"""

# Series 데이터 구조와 생성
import pandas as pd

s1 = pd.Series([10, 20, 30, 40, 50])    # 리스트로 Series 데이터 생성
print('- pd.Series([10, 20, 30, 40, 50]):\n{0}'.format(s1))

# Series 데이터는 index와 values를 분리해 가져올 수 있다.
print('- s1.index:\n{0}'.format(s1.index))
print('- s1.values:\n{0}'.format(s1.values))

# 날짜별 판매량을 생성하는 예시
import numpy as np

index_data = ['2020-02-07', '2020-02-28', '2020-02-29', '2020-03-01']   # 날짜 지정
data = [3500, 3579, np.nan, 3782]   # 데이터 지정 (np.nan == not a number)

s2 = pd.Series(data, index=index_data)
print('- pd.Series(data, index=index_data):\n{0}'.format(s2))

# 딕셔너리 데이터로부터 Series 데이터를 생성하는 예시
s3 = pd.Series({'국어': 100, '영어': 95, '수학': 90})
print("- pd.Series({'국어': 100, '영어': 95, '수학': 90}):")
print(s3)

# 판다스의 date_range()를 이용해 날짜를 생성하는 예시
index_data = pd.date_range(start='2020-02-27', end='2020-03-01')    # 날짜 생성
data = [3500, 3579, np.nan, 3782]
print("- index_data = pd.date_range(start='2020-02-27', end='2020-03-01'):")
print(pd.Series(data, index=index_data))

# 판다스의 Series 데이터를 재배열하는 방법
print('- 판다스의 Series 데이터를 재배열하는 방법')
s4 = pd.Series({'B': 4.0, 'A': 5.0, 'D': 2.0, 'C': 3.0})
print("pd.Series({'B': 4.0, 'A': 5.0, 'D': 2.0, 'C': 3.0}):")
print(s4)
print("s4.reindex(['A', 'B', 'C', 'D']):")
print(s4.reindex(['A', 'B', 'C', 'D']))

