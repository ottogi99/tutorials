"""
행렬의 행과 열을 바꾸는 것을 전치(transpose)라고 하며, 판다스에서는 다음과 같은 방법으로 DataFrame 데이터의 행과 열을 바꿀 수 있습니다.
DataFrame.T
"""
import pandas as pd
import numpy as np

dict_data = {'A': [0, 1, 2, 3],
             'B': [4, 5, 6, 7],
             'C': [8, 9, 10, 11]}
index_data = ['a', 'b', 'c', 'd']

df1 = pd.DataFrame(dict_data, index=index_data)
print("pd.DataFrame(dict_data, index=index_data)=\n{0}".format(df1))

print("\n- df1 의 전치를 구하는 예시")
print("\ndf1.T=\n{0}".format(df1.T))
