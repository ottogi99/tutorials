"""
일 년간의 관측값이 저장된 데이터 파일에서 월별로 각 지점의 기본 통계량을 구하고 싶은 경우 처리
"""

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False


def write_stat_data_box_plot_to_excel_sheet(write_excel_file, df_months):
    excel_writer = pd.ExcelWriter(write_excel_file, engine='xlsxwriter')

    for month_num, df_month in enumerate(df_months):
        df_month_stat = df_month.describe()

        # 시트 이름 생성
        sheet = "{0:2d}월".format(month_num + 1)

        # 날짜 열을 datetime 형식에 문자열로 변환
        df_month['날짜'] = df_month['날짜'].astype(str)

        # DataFrame 데이터의 '날짜'열을 index로 지정
        df_month = df_month.set_index(['날짜'])

        # DataFrame 데이터를 생성한 엑셀 객체에 쓰기
        df_month.to_excel(excel_writer, sheet_name=sheet)

        # 워크시트에 위치를 지정해 기본 통계량 데이터(df_month_stat) 쓰기
        row = 0
        col = len(df_month.columns) + 2
        df_month_stat.to_excel(excel_writer, sheet_name=sheet, startrow=row, startcol=col)

        # --- 박스 그래프 그리고 이미지 파일로 저장하기 ---
        ax = df_month.plot.box(y=["A지점", "B지점", "C지점"], showmeans=True)
        ax.set_ylabel("일일 판매량", fontsize=15)
        ax.set_title("지점별 일일 판매량 분포", fontsize=20)

        # 박스 그래프의 이미지 파일 경로
        image_file = folder + "지점별_일일_판매량_분포_{0:02d}월.png".format(month_num + 1)

        plt.savefig(image_file, dpi=300)
        plt.close()
        # -------------------------------------------

        worksheet = excel_writer.sheets[sheet]

        row = len(df_month_stat.index) + 2
        col = len(df_month.columns) + 2
        worksheet.insert_image(row, col, image_file, {'x_scale': 0.6, 'y_scale': 0.6})

        excel_writer.save()


folder = './data/ch09/'
csv_file = folder + '2019년_지점별_일일_판매량.csv'
df = pd.read_csv(csv_file)

# 데이터 타입을 확인
# print(df.info())

# 날짜 열의 데이터 타입이 object 이므로 to_datetime()을 통해 datetime 형식을 변환
df['날짜'] = pd.to_datetime(df['날짜'])
# print(df.info())

"""
DataFrame 데이터 메서드인 groupby()와 판다스의 Grouper()로 날짜 열에 대해 월별로 그룹을 만들어 리스트로 변환
"""
df_months = [group for name, group in df.groupby(pd.Grouper(key='날짜', freq='M'))]
print(df_months[0].head())

# 저장할 엑셀 파일
folder = './data/ch09/'
excel_file = folder + '2019년_지점별_일일_판매량_기본통계량_박스그래프.xlsx'

# DataFrame 데이터, 기본 통계량, 박스 그래프를 엑셀 파일에 쓰는 함수 호출
write_stat_data_box_plot_to_excel_sheet(excel_file, df_months)

print("생성 파일:", excel_file)

