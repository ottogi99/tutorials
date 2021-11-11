"""
DataFrame 데이터 구조와 생성
판다스의 DataFrame은 말 그대로 자료(Data)를 담는 틀(Frame)인데
이를 이용하면 행과 열이 있는 표 형식의 데이터를 생성할 수 있습니다.
"""

# DataFrame 데이터를 생성하는 예시
import pandas as pd

data = [[1,2,3], [4,5,6], [7,8,9]]
df = pd.DataFrame(data)
print('- DataFrame 데이터를 생성하는 예시')
print('data = [[1,2,3], [4,5,6], [7,8,9]]')
print('pd.DataFrame(data):\n{0}'.format(df))

# 넘파이의 배열을 이용해 DataFrame 데이터를 생성하는 예시
import numpy as np

data = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
index_data = pd.date_range('2020-01-11', periods=4)
columns_data = ['A', 'B', 'C']
print('- 넘파이의 배열을 이용해 DataFrame 데이터를 생성하는 예시')
pd.DataFrame(data, index=index_data, columns=columns_data)
print('pd.DataFrame(data, index=index_data, columns=columns_data):')
print(pd.DataFrame(data, index=index_data, columns=columns_data))

# DataFrame 데이터 생성을 위해 딕셔너리를 이용하는 예시
print('-DataFrame 데이터 생성을 위해 딕셔너리를 이용하는 예시')
dict_data = {'연도': [2017, 2017, 2018, 2018, 2019, 2019],
             '지사': ['한국', '미국', '한국', '미국', '한국', '한국'],
             '고객수': [200, np.nan, 250, 450, 300, 500]}

df = pd.DataFrame(dict_data)
print("dict_data = {\n"
      "'연도': [2017, 2017, 2018, 2018, 2019, 2019],\n"
      "'지사': ['한국', '미국', '한국', '미국', '한국', '한국'],\n"
      "'고객수': [200, np.nan, 250, 450, 300, 500]\n"
      "}")
print('pd.DataFrame(dict_data):\n{0}'.format(df))

# DataFrame 데이터에서 index, columns, values 는 각각 df.index, df.columns, df.values로 확인할 수 있습니다.
print('-- DataFrame 데이터에서 index, columns, values 는 각각 df.index, df.columns, df.values로 확인')
print('df.index: {0}'.format(df.index))
print('df.columns: {0}'.format(df.columns))
print('df.values:\n{0}'.format(df.values))

# DataFrame 데이터의 특정 열을 이용해 index를 변경하고 싶다면 df.set_index(열_이름)을 이용합니다.
print('-- DataFrame 데이터의 특정 열을 이용해 index를 변경하고 싶다면 df.set_index(열_이름)을 이용합니다.')
df1 = df.set_index("연도")
print('df.set_index("연도"):\n{0}'.format(df1))

# 판다스의 DataFrame 데이터에 reindex(new_index_data)를 적용하면 행 데이터를 재배열해 반환하고
# reindex(columns=new_columns_data)를 적용하면 열 데이터를 재배열해 반환합니다.
print("-- 판다스의 DataFrame 데이터에 reindex(new_index_data)를 적용하면 행 데이터를 재배열해 반환하고"
      "reindex(columns=new_columns_data)를 적용하면 열 데이터를 재배열해 반환합니다.")
dict_data = {'A': [10,20,30,40,50,60],
            'B': [0.1,0.2,0.3,0.4,0.5,0.6],
            'C': [100,200,300,400,500,600]}

print("dict_data = {'A': [10,20,30,40,50,60],"
      "'B': [0.1,0.2,0.3,0.4,0.5,0.6],"
      "'C': [100,200,300,400,500,600]}")
df2 = pd.DataFrame(dict_data)
print('pd.DataFrame(dict_data):\n{0}'.format(df2))
print("- reindex(new_index_data)를 이용해 새로운 index로 DataFrame 데이터의 행 데이터 재배열")
print("df2.reindex([4,2,5,3,1]):\n{0}".format(df2.reindex([4,2,5,3,1])))

print('-reindex(columns=new_columns_data) 를 이용해 새로운 columns로 DataFrame 데이터의 열 데이터 재배열')
df2 = df2.reindex(columns=['B', 'C', 'A'])
print("df2.reindex(columns=['B', 'C', 'A']):\n{0}".format(df2))
