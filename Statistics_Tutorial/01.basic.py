"""
엑셀의 기본 통계량 함수

통계량     엑셀함수        사용예
관측수     COUNT()
합계      SUM()
평균      AVERAGE()
중앙값     MEDIAN()
최솟값     MIN()
최댓값     MAX()
최빈값     MODE.SNGL()
분산      VAR.P()         모집단의 분산
        VAR.S()         표본의 분산
표준편차    STDEV.P()       모집단의 표준편차
            STDEV.S()       표본의 표준편차
"""

import pandas as pd

folder = './data/ch09/'
csv_file = folder + '지점별_일일_판매량.csv'

df = pd.read_csv(csv_file, index_col='날짜')

print(df.head())

"""
describe() 메서드를 이용하면 각 열의 데이터 개수, 평균, 표준편차, 최솟값, 최댓값, 사분위수를 한 번에 계산할 수 있음.
"""
df_stat = df.describe()
print(df_stat)

"""
그래프를 그려보면 좀 더 직관적으로 데이터의 분포를 살펴볼 수 있습니다.
"""
import matplotlib
import matplotlib.pyplot as plt

# 한글 폰트를 위한 설정
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

# 박스 그래프 그리기
ax = df.plot.box(y=["A지점", "B지점", "C지점"], showmeans=True)
ax.set_ylabel("일일 판매량", fontsize=15)
ax.set_title("지점별 일일 판매량 분포", fontsize=20)

# 엑셀 파일에 추가할 그래프 이미지 파일
image_file = './figures/지점별_일일_판매량_분포.png'

plt.savefig(image_file, dpi=300)
plt.show()
