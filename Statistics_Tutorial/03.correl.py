"""
상관계수
상관계수를 구할때 가장 많이 사용하는 방법은 피어슨(Pearson) 상관계수를 사용
피어슨 상관계수의 절댓값이 1에 가까울수록 관측값이 가상의 일직선상에 가깝게 모여 있고
0에 가까울수록 흩어지는 것을 볼 수 있다.
또한 상관계수의 값이 양수(음수)이면 가상 일직선의 기울기가 양수(음수)인 것을 확인할 수 있다.
"""

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

folder = './data/ch09/'
csv_file = folder + '기온별_아이스_커피_판매량.csv'

df = pd.read_csv(csv_file)

print(df.head())

ax_scatter = df.plot.scatter(x='기온', y='아이스커피판매량', grid=True)

ax_scatter.set_xlabel("기온 (섭씨)", fontsize=15)
ax_scatter.set_ylabel("아이스 커피 판매량", fontsize=15)
ax_scatter.set_title("기온별 아이스 커피 판매량", fontsize=20)

plt.show()

"""
판다스 DataFrame 데이터(df)에 대해 모든 열끼리(자신의 열 포함)의 상관 계수는 corr()를 이용해 구합니다.
* 기온과 아이스 커피 판매량의 상관 계수는 0.982405로 확인 가능
"""
print(df.corr())


"""
여러 변수 사이의 상관 분석
"""
folder = './data/ch09/'
csv_file = folder + 'iris_setosa_data.csv'
df = pd.read_csv(csv_file)
print("\n- 여러 변수 사이의 상관 분석")
print(df.head())

"""
판다스에서는 DataFrame 데이터에 scatter_matrix()를 적용해 두 개의 변수 간의 산점도와 한 변수에 대한 히스토그램을 한 번에 그릴 수 있는 기능을 제공합니다.
* 아래 출력된 그래프를 보면 sepal_length와 sepal_width 변수를 이용해 그린 산점도가 양의 상관관계가 가장 큰 것을 볼 수 있습니다.
"""
from pandas.plotting import scatter_matrix

scatter_matrix(df, alpha=1, figsize=(8, 8))
plt.show()

print("\n- 각 변수간의 상관 계수는 다음과 같다.")
print("\n- sepal_length와 sepal_width 변수 간에 상관관계가 가장 강한 것을 알 수 있다.")
print(df.corr())

