"""
회귀분석
관측한 변수들에 대해 독립변수 x와 종속변수 y 사이의 관계를 수학적 모델(함수)을 만들어 미래를 예측하는 회귀분석에 대해 알아봅니다.

선형 회귀 모델
: 회귀 분석을 진행한 후에 모델의 적합도는 결정 계수 R^2으로 판단할 수 있습니다.
R^2이 1에 가까울수록 모델의 적합도는 올라가고 0에 가까울수록 적합도는 떨어집니다.

단순 선형 회귀 분석
# (1) LinearRegression 객체(model)를 생성
model = LinearRegression()
# (2) fit() 메서드로 회귀분석 수행. 입력은 X, y
model.fit(X, y)
# (3) predict() 메서드로 입력 X_new에 대한 y_hat 추정
y_hat = model.predict(X_new)
"""

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression


folder = './data/ch09/'
csv_file = folder + '기온별_아이스_커피_판매량.csv'
df = pd.read_csv(csv_file)
# print(df.head())

X = df['기온'].values.reshape(-1, 1)  # X는 행렬 (X는 n * p 행렬 형태를 갖춰야 하므로 reshape(-1, 1)을 적용
y = df['아이스커피판매량'].values       # y는 백터

model = LinearRegression().fit(X, y)

beta0 = model.intercept_
beta1 = model.coef_[0]

"""
선형 회귀 분석 결과로부터 기온(x)와 아이스 커피 판매량(y) 사이에는 y=-33.8412 + 7.9186x 의 관계가 있음을 알 수 있습니다.
"""
print("beta0 = {0:.4f}, beta1 = {1:.4f}".format(beta0, beta1))

"""
선형 회귀 분석 결과의 X를 이용해 y의 추정값을 구한 후에 결정 계수(R^2)를 게산하는 코드
"""
y_hat = model.predict(X)

SST = np.sum((y - np.mean(y)) ** 2)
SSR = np.sum((y_hat - np.mean(y)) ** 2)
SSE = np.sum((y - y_hat) ** 2)

R_squared = 1 - SSE / SST

print("결정 계수: {0:.4f}".format(R_squared))


"""
사이킷런의 서브 패키지인 metrics의 r2_score()를 이용하여 간편하게 구하기
"""
from sklearn.metrics import r2_score

r2_score(y, y_hat)

"""
선형 회귀 분석으로 구한 추세선을 산점도 그래프에 함께 모두 표시하면 선형 회귀 분석 결과를 시각적으로 확인할 수 있습니다.
"""
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

plt.scatter(X, y)   # 산점도 그리기
plt.grid(True)      # 격자 추가
plt.xlabel("기온 (섭씨)", fontsize=15)              # x축 라벨
plt.ylabel("아이스 커피 판매량", fontsize=15)           # y 축 라벨
plt.title("기온별 아이스 커피 판매량", fontsize=20)        # 그래프 제목

# 추세선 표시
x_data = np.array([10, 40])     # 추세선을 위한 x축 데이터
y_data = beta0 + beta1 * x_data  # 추세선을 위한 y축 데이터

plt.plot(x_data, y_data, 'r--')     # y = beta_0 + beta_1 * x 에 해당하는 선을 그림

# 추세선 수식을 그래프에 표시
eq_text = "y={0:.4f} + {1:.4f}x".format(beta0, beta1)   # 그래프에 표시할 문자열 생성
plt.text(12, 250, eq_text, fontsize=15)                 # 지정한 위치(x, y) = (12, 250)에 문자열 표시

plt.show()

"""
회귀 분석을 하는 목적은 주어진 데이터로 실제로는 없는 데이터를 예측하는 것입니다.
앞에서 기온(x)과 아이스 커피 판매량(y) 사이에는 y= -33.8412 + 7.9186x 의 관계가 있음을 알았으므로 
일기 예보를 통해 확인한 오늘의 최고 기온으로 오늘의 아이스 커피 판매량을 예측할 수 있습니다.
만약 최고 기온 38.5도라면
"""
high_temp = [38.5]
X_new = np.array(high_temp).reshape(-1, 1)

y_hat = model.predict(X_new)

print("- 최고 기온: ", high_temp)
print("- 아이스 커피 예상 판매량: ", y_hat)

# 새로운 독립 변수 X_new 생성
high_temps = [23.2, 38.5, 39.1]
X_new = np.array(high_temps).reshape(-1, 1)

y_hat = model.predict(X_new)

# 추정 결과를 이용해 DataFrame 데이터 생성
ice_coffees = y_hat.astype(int) # 실수를 정수로 변환 후 ice_coffees에 할당
df_new = pd.DataFrame({'기온_new': high_temps, '아이스커피_예상_판매량:': ice_coffees})
print(df_new)

"""
다중 선형 회귀 분석
여러 개의 독립 변수(온도, 습도, CO2)와 하나의 종속 변수(수확량)로 구성
이를 이용해 다중 선형 회귀 분석을 수행하면 환경 요소(온도, 습도, 이산화탄소 농도)가 작물의 수확량에 얼마나 영향을 주는지 알 수 있습니다.
"""
folder = './data/ch09/'
csv_file = folder + '환경별_수확량.csv'

df = pd.read_csv(csv_file)
print("\n- 다중 회귀 분석")
print(df.head())

"""
seaborn 라이브러리는 matplotlib을 기반으로 만든 시각화 라이브러리로 matplotlib에 비해 색상 표현이 뛰어난 테마와 사용이 편리한 그래프 기능을 제공
"""
import seaborn as sns

sns.pairplot(df, height=1.8)
plt.show()

X = df[['온도', '습도', 'CO2']].values  # X는 행렬 (독립변수 x1, x2, x3의 관측값)
y = df['수확량'].values                # y는 벡터 (y의 관측값)

# LinearRegression 객체(model)에 대해 fit() 메서드로 회귀 분석 수행
model = LinearRegression().fit(X, y)

# 파라미터 추정값 결과 출력
print("- y 절편 상수:", model.intercept_)   # beta0
print("- x의 가중치 벡터:", model.coef_)      # [beta1, beta2, beta3]

"""
위 다중 선형 회귀 분석 결과로 구한 추정 파라미터 (b0 = 436.439, b1=2.76614, b2=1.70455, b3=0.23201) 구함
선형 회귀 분석 후에는 다음과 같이 predict()를 이용해 y를 추정한 값을 구한 후 r2_score()로 결정 계수를 구할 수 있습니다.
"""
from sklearn.metrics import r2_score

y_hat = model.predict(X)
print(r2_score(y, y_hat))

"""
독립변수 x1, x2, x3의 관측값이 n개 주어졌을 때 각 관측값에 대한 추정값 y을 구합니다.
"""
# 새로운 독립 변수 X_new 생성
temp = [17.7, 27.8, 16.8, 15.2, 39.7]   # 온도
humi = [69.2, 69.9, 48.0, 62.3, 37.4]   # 습도
co2 = [743.7, 839.6, 770.5, 577.6, 839.3]   # CO2 농도

X_new = np.array([temp, humi, co2]) # 각 측정값을 행렬(2차원 배열)로 만듦
X_new = X_new.T                     # n x p 행렬을 만들기 위해 행렬의 전치(transpose)를 수행
print(X_new)

"""
이제 predict()로 X_new에 대한 추정을 하고 추정 결과를 DataFrame 데이터로 만드는 코드를 작성하면 다음과 같습니다.
"""
y_hat = model.predict(X_new)

df_new = pd.DataFrame({'온도': temp, '습도': humi, "CO2": co2, '예상수확량:': y_hat})
df_new.style.format('{:.1f}')   # DataFrame 데이터의 출력 형식을 지정
print(df_new)
