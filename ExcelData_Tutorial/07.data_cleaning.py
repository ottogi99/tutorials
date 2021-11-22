"""
엑셀 파일 워크시트 데이터에서 누락 데이터를 찾고 처리하는 방법과 데이터에서 원하는 데이터 값만 추출해 정리하는 방법을 살펴봅니다.

DataFrame_data.info() : index와 column의 범위, 데이터의 타입, 결측치가 아닌 값의 개수와 메모리 사용 정보 등을 요약
DataFrame_data.isnull()
DataFrame_data.notnull()
"""

import pandas as pd
import numpy as np
import xlwings as xw
from pathlib import Path


folder = './data/ch07/missing_data/'
excel_file = folder + '자동차판매현황.xlsx'
df = pd.read_excel(excel_file, index_col='연도')

"""
누락 데이터 확인
"""
# print(df.info())
# print(df.isnull())
# print(df.isnull().sum())
# print(df.notnull())
# print(df.notnull().sum())

"""
누락 데이터 처리
DataFrame_data.dropna([axis=0 (or 1), how='any' (or 'all'), thresh = 정수, subset = 라벨])
 axis: 제거하고자 하는 데이터의 축을 지정 [0(index): 행의 결측치 확인 제거, 1(columns): 열의 결측치 확인 제거]
 how: 'any'로 지정하면 행 혹은 열에 하나라도 결측치가 있으면 행 혹은 열을 제거, 'all'로 지정하면 행 혹은 열의 모든 데이터가 결측치인 경우 행 혹은 열을 제거
 thresh: 해당 정수 미만일 때만 행이나 열을 제거
 subset: 제거하고자 하는 행 혹은 열과 다른 축의 라벨을 지정해 결측치를 확인할 기준을 설정
"""
dropna_axis_index = df.dropna(axis=0)
print(dropna_axis_index)

dropna_axis_columns = df.dropna(axis=1, thresh=4)
print(dropna_axis_columns)

dropna_subset = df.dropna(axis=1, subset=[2018, 2019])
print(dropna_subset)

"""
결측치에 특정 값을 채우는 방법
DataFrame_data.fillna(value=None, method=None, axis=None)
"""
fillna_zero = df.fillna(0)      # 모든 결측치를 0으로 채움 `df.fillna(value=0)`과 동일
print(fillna_zero)

fillna_content = df.fillna('누락')    # `df.fillna(value='누락')`
print(fillna_content)

"""
데이터 열의 결측치를 다음 index의 비결측치로 채우고 싶으면 method='bfill' 을 인수로 입력
만약 다음 index의 값도 결측치라면 비결측치가 나올 때까지 계속해서 그 다음 값을 찾아 결측치를 채웁니다.
"""
fillna_bfill = df.fillna(method='bfill')    # df.fillna(method='bfill', axis=0)
print(fillna_bfill)

"""
데이터 열의 결측치를 이전 index의 비결측치로 채우고 싶으면 method='ffill'을 인수로 입력
만약 이전 이전 index의 값도 결측치라면 비결측치가 나올 때까지 계속해서 그 이전 값을 찾아 결측치를 채웁니다.
"""
fillna_ffill = df.fillna(method='ffill')    # df.fillna(method='ffill', axis=0)
print(fillna_ffill)

"""
데이터의 열별도 다른 값을 채우고 싶은 경우 딕셔너리 형식으로 열 이름과 채울 값을 지정할 수 있음
"""
values = {"세단A": 500, "트럭X": 200, "왜건K": 0, "밴Q": 0}
fillna_values = df.fillna(values)   # df.fillna(value=values)
print(fillna_values)



