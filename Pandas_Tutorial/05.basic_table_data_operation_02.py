"""
표 데이터의 집계 및 통계연산
sum(), mean(), std(), var(), min(), max(), cumsum(), cumprod()

- 메서드 옵션에서 axis=0으로 지정하면 DataFrame 데이터의 values에서 index 방향으로 연산 수행 (기본값)
- 메서드 옵션에서 axis=1으로 지정하면 DataFrame 데이터의 values에서 columns 방향으로 연산 수행
"""
import pandas as pd

csv_file = "./data/ch05/korea_rain1.csv"

df = pd.read_csv(csv_file, encoding='utf8', index_col='연도')
print("- pd.read_csv(csv_file, encoding='utf8', index_col='연도')")
print(df)

# 평균과 표준편차
print("- 평균) df.mean():\n", df.mean())
print("- 표준편차) df.std():\n", df.mean())
print("- df.mean(axis=1):\n", df.mean(axis=1))
print("- df.std(axis=1):\n", df.std(axis=1))

# 평균, 표준편차, 최솟값, 최댓값 등 기본 통계량을 한꺼번에 구할 수 있는 describe() 메서드
print("- 기본 통계량 표출) df.describe():\n", df.describe())

