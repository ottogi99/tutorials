"""
표 데이터 선택
판다스의 Series 데이터와 DataFrame 데이터에서 특정한 행이나 열 데이터를 선택하거나,
원하지 않는 데이터를 삭제하는 방법
"""
import pandas as pd
import numpy as np

# Series에서 행 데이터 선택하는 예시
index_data = ['a', 'b', 'c', 'd', 'e']
data = [0.0, 1.0, 2.0, 3.0, 4.0]
s1 = pd.Series(data, index=index_data)

# Series에서 행 데이터 선택하는 예시 (index 라벨 지정)
print("- Series에서 행 데이터 선택하는 예시 (index 라벨 지정)")
print("s1=\n{0}".format(s1))
print("s1.loc['a']=", s1.loc['a'])
print("s1.loc[['a','c','e']]=\n{0}".format(s1.loc[['a','c','e']]))
print("s1.loc['b':'d']=\n{0}".format(s1.loc['b':'d']))

# Series에서 인행 데이터 선택하는 예시 (위치 지정)
print("- Series에서 인행 데이터 선택하는 예시 (위치 지정)")
print("s1.iloc[1]=", s1.iloc[1])
print("s1.iloc[[0,2,4]]=\n{0}".format(s1.iloc[[0,2,4]]))
print("s1.iloc[1:4]=\n{0}".format(s1.iloc[1:4]))

# 선택한 행 데이터에 스칼라 값을 지정
print("- 선택한 행 데이터에 스칼라 값을 지정")
s1.loc['a':'c'] = 10
print("s1.loc['a':'c'] = 10\n{0}".format(s1))
s1.iloc[3:5] = 20
print("s1.iloc[3:5] = 20\n{0}".format(s1))

#
dict_data = {'A': [0,10,20,30,40],
             'B': [0,0.1,0.2,0.3,0.4],
             'C': [0,100,200,300,400]
             }
index_data = ['a','b','c','d','e']

df1 = pd.DataFrame(dict_data, index=index_data)
print('df1 =\n{0}'.format(df1))
# index 라벨 지정으로 행 데이터를 선택
print('index 라벨 지정으로 행 데이터를 선택')
print("df1.loc['a']:\n{0}".format(df1.loc['a']))
print("df1.loc[['a','c','e']]:\n{0}".format(df1.loc[['a','c','e']]))
print("df1.loc['b':'d']:\n{0}".format(df1.loc['b':'d']))
# index 위치 지정으로 행 데이터를 선택
print('index 위치 지정으로 행 데이터를 선택')
print("df1.iloc[2]:\n{0}".format(df1.iloc[2]))
print("df1.iloc[[1,3,4]]:\n{0}".format(df1.iloc[[1,3,4]]))
print("df1.iloc[1:3]:\n{0}".format(df1.iloc[1:3]))

# 선택한 행 데이터에 스칼라 값을 지정
print("- 선택한 행 데이터에 스칼라 값을 지정")
df1.loc['a':'c'] = 50
print("df1.loc['a':'c'] = 50\n{0}".format(df1))
df1.iloc[3:5] = 60
print("df1.iloc[3:5] = 60\n{0}".format(df1))

# 판다스의 Series는 loc나 iloc 없이도 index 위치나 라벨을 바로 지정해 행 데이터를 선택할 수 있음
print("\n- 판다스의 Series는 loc나 iloc 없이도 index 위치나 라벨을 바로 지정해 행 데이터를 선택할 수 있음")
index_data = ['a','b','c','d','e']
data = [0,1,2,3,4]

s2 = pd.Series(data, index=index_data)
print("pd.Series(data, index=index_data):\n{0}".format(s2))

print("s2['a']=\n{0}".format(s2['a']))
print("s2[['a', 'c']]=\n{0}".format(s2[['a', 'c']]))
print("s2['c':'e']=\n{0}".format(s2['c':'e']))
print("s2['a':'e':2]=\n{0}".format(s2['a':'e':2]))
print("s2[0]=\n{0}".format(s2[0]))
print("s2[[1,2,4]]=\n{0}".format(s2[[1,2,4]]))
print("s2[0:5:2]=\n{0}".format(s2[0:5:2]))

# 판다스의 Series 데이터나 DataFrame 데이터에 조건을 지정해 행 데이터를 선택
print("\n- [ 판다스의 Series 데이터나 DataFrame 데이터에 조건을 지정해 행 데이터를 선택 ]")
s = pd.Series(range(-3, 6))
print("\n- pd.Series(range(-3, 6)) = \n{0}".format(s))

dict_data = {'지점': ['서울', '대전', '대구', '부산', '광주'],
            '1월': [558, 234, 340, 380, 213],
            '2월': [437, 216, 238, 290, 194],
            '3월': [337, 196, 209, 272, 186],
            }
df = pd.DataFrame(dict_data)

print("\n- pd.DataFrame(dict_data)=\n{0}".format(pd.DataFrame(dict_data)))
print("\n- s[(s >= -2) & (s%2 == 0)]=\n{0}".format(s[(s >= -2) & (s%2 == 0)]))
print("\n- df[df['1월'] >= 300]=\n{0}".format(df[df['1월'] >= 300]))
print("\n- df[(df['지점'] == '서울') | (df['지점'] == '부산')]=\n{0}".format(df[(df['지점'] == '서울') | (df['지점'] == '부산')]))
# isin() 메서드를 이용해서 Series나 DataFrame 데이터의 불 인덱싱 기능을 수행
print("\n- df[df['지점'].isin(['서울','부산'])=\n{0}".format(df[df['지점'].isin(['서울','부산'])]))


# 전체 데이터 중 처음이나 끝 일부 행만 선택해 출력
dict_data = {'제품ID': ['P501', 'P502', 'P503', 'P504', 'P505', 'P506', 'P507'],
             '판매가격': [6400, 5400, 9400, 10400, 9800, 1200, 3400],
             '판매량': [63, 56, 98, 48, 72, 59, 43],
             '이익률': [0.30, 0.21, 0.15, 0.25, 0.45, 0.47, 0.32]
             }
df2 = pd.DataFrame(dict_data)
print("\n- pd.DataFrame(dict_data)=\n{0}".format(df2))
print("\ndf2.head()=\n{0}".format(df2.head()))
print("\ndf2.head(2)=\n{0}".format(df2.head(2)))
print("\ndf2.tail()=\n{0}".format(df2.tail()))
print("\ndf2.tail(3)=\n{0}".format(df2.tail(3)))

# 열 데이터 선택
print("\n-- [ 열 데이터 선택 ]")
print("\ndf2['제품ID']\n{0}".format(df2['제품ID']))
print("\ndf2[['제품ID','이익률','판매가격']]\n{0}".format(df2[['제품ID','이익률','판매가격']]))
print("-- 지정한 열 데이터의 모든 값을 스칼라값을 변경")
df2['이익률'] = 0.5
print("df2['이익률'] = 0.5\n{0}".format(df2))

# 행과 열 데이터 선택
print("\n-- [ 행과 열 데이터 선택 ]")
dict_data = {'A': [0, 1, 2, 3, 4],
             'B': [10, 11, 12, 13, 14],
             'C': [20, 21, 22, 23, 24]}
index_data = ['a', 'b', 'c', 'd', 'e']
df = pd.DataFrame(dict_data, index=index_data)
print("pd.DataFrame(dict_data, index=index_data)=\n{0}".format(df))
print("\n- loc 이용")
print("df.loc['a', 'A']={0}".format(df.loc['a', 'A']))
print("df.iloc[0, 0]={0}".format(df.iloc[0, 0]))
print("df.loc['a':'c', ['A', 'B']]=\n{0}".format(df.loc['a':'c', ['A', 'B']]))
print("df.iloc[0:3, 0:2]=\n{0}".format(df.iloc[0:3, 0:2]))
print("\n- 조건을 지정해 행을 선택")
print("df.loc[df['A'] > 2, ['A', 'B']]=\n{0}".format(df.loc[df['A'] > 2, ['A', 'B']]))
print("\n- 스칼라 값 지정")
df.loc['a':'c', ['A', 'B']] = 50
print("df.loc['a':'c', ['A', 'B']] = 50\n{0}".format(df))
df.iloc[3:5, 1:3] = 100
print("df.iloc[3:5, 1:3] = 100\n{0}".format(df))
df.loc[df['B'] < 70, 'B'] = 70
print("df.loc[df['B'<70, 'B']] = 70\n{0}".format(df))
print("\n- 기존 데이터에 없는 경우 새롭게 열 이름을 생성해 열 데이터를 추가 (D column)")
df.loc[df['C'] < 30, 'D'] = 40
print("df.loc[df['C'] < 30, 'D'] = 40\n{0}".format(df))

print("\n - 열 이름(column_name)만 지정해 열 데이터를 선택하는 경우에 행데이터 지정")
dict_data = {'A': [0, 1, 2, 3],
             'B': [4, 5, 6, 7],
             'C': [8, 9, 10, 11]}
index_data = ['a', 'b', 'c', 'd']

df1 = pd.DataFrame(dict_data, index=index_data)
print("pd.DataFrame(dict_data, index=index_data)=\n{0}".format(df1))
print("\ndf1['C']['c']=\n{0}".format(df1['C']['c']))
print("\ndf1['C'][0,1,3]=\n{0}".format(df1['C'], [0, 1, 3]))
print("\ndf1['C']['a':'d']=\n{0}".format(df1['C']['a':'d']))
print("\ndf1['C'][df1['B']>=5]=\n{0}".format(df1['C'][df1['B']>=5]))

