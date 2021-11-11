"""
CSV 파일이나 엑셀 파일에서 데이터를 읽어와서 판다스 DataFrame 데이터를 생성하고
DataFrame 데이터를 CSV 파일이나 엑셀 파일로 저장하는 방법을 확인
"""

# DataFrame 데이터를 생성하는 예시
import pandas as pd

# CSV 파일 경로
# folder = 'C:/Repo/python/tutorials/Pandas_Tutorial/data/ch05/'
folder = './data/ch05/'
csv_file = folder + 'korea_rain1.csv'

print('- CSV 파일을 읽어와서 DataFrame 데이터 생성')
df = pd.read_csv(csv_file, encoding='utf-8')
print("pd.read_csv(csv_file, encoding='utf-8'):\n{0}".format(pd.read_csv(csv_file, encoding='utf-8')))

print('- 특정 열을 index로 지정하여 DataFrame 생성')
df = pd.read_csv(csv_file, sep=',', index_col='연도')
print("pd.read_csv(csv_file, index_col='연도'):\n{0}".format(pd.read_csv(csv_file, sep=',', index_col='연도')))

# 구분자가 tab인 경우
print('- 구분자가 tab으로 필드 사이가 구분된 경우 예시')
df = pd.read_csv(csv_file, sep='\t')
csv_file = folder + 'korea_rain1_tab.txt'
print("pd.read_csv(csv_file, sep='\\t'):\n{0}".format(pd.read_csv(csv_file, sep='\t')))

print('- 열 이름이 없는 CSV 파일을 DataFrame 데이터로 읽어올 때 header=None을 지정')
csv_file = folder + 'korea_rain2.csv'
print("pd.read_csv(csv_file, header=None):\n{0}".format(pd.read_csv(csv_file, header=None)))

print('- 열 이름이 없는 CSV 파일을 DataFrame 데이터로 읽어올 때 columns를 명시적으로 지정')
csv_file = folder + 'korea_rain2.csv'
names_list = ["Year", "Spring", "Summer", "Fall", "Winter"]
print('names_list: {0}'.format(names_list))
df2 = pd.read_csv(csv_file, names=names_list)
print("pd.read_csv(csv_file, names=names_list):\n{0}".format(pd.read_csv(csv_file, names=names_list)))

print('- 첫 줄에 열 이름이 있는 CSV 파일을 DataFrame 데이터로 읽어올 때 columns를 변경 (header=0)')
csv_file = folder + 'korea_rain1.csv'
names_list = ["연도_new", "봄_new", "여름_new", "가을_new", "겨울_new"]
print('names_list: {0}'.format(names_list))
df2 = pd.read_csv(csv_file, header=0, names=names_list)
print("pd.read_csv(csv_file, header=0, names=names_list):\n{0}".format(pd.read_csv(csv_file, header=0, names=names_list)))

print('- to_csv() 이용해 DataFrame 데이터를 CSV 파일로 저장')
df = pd.DataFrame({'제품ID': ['P1001','P1002','P1003','P1004'],
                   '판매가격': [5000, 7000, 8000, 10000],
                   '판매량': [50, 93, 70, 48]})

print(df)
csv_file = folder + 'output1.csv'
print("df.to_csv({0})".format(csv_file))
df.to_csv(csv_file)
print("생성한 CSV 파일: {0}", csv_file)

print("- DataFrame 데이터를 CSV 파일로 쓰기(인코딩은 'cp949', index 포함 안함)")
csv_file = folder + 'output_cp949_encoding.csv'
print("df.to_csv({0}, encoding='cp949', index=False)".format(csv_file))
df.to_csv(csv_file, encoding='cp949', index=False)
print("생성한 CSV 파일: {0}", csv_file)


# 엑셀 파일 읽고 쓰기
excel_file = folder + '사원별_월간_판매현황.xlsx'
df = pd.read_excel(excel_file)
print("- pd.read_excel(excel_file):\n{0}".format(pd.read_excel(excel_file)))

df = pd.read_excel(excel_file, index_col='이름')
# df = pd.read_excel(excel_file, index_col=0)   # 이 방법도 가능
print("- pd.read_excel(excel_file, index_col='이름'):\n{0}".format(pd.read_excel(excel_file, index_col='이름')))

# 워크시트가 두 개 이상일 때 shee_name 옵션으로 가져올 위크시트 지정
excel_file = folder + '사원별_월간_판매현황2.xlsx'
df = pd.read_excel(excel_file, sheet_name='하반기')
# df = pd.read_excel(excel_file, sheet_name=1)
print("- pd.read_excel(excel_file, sheet_name='하반기'):\n{0}".format(df))

df = pd.read_excel(excel_file, sheet_name='하반기', index_col='이름')
print("- pd.read_excel(excel_file, sheet_name='하반기', index_col='이름'):\n{0}".format(df))

excel_file = folder + '사원별_월간_판매현황_열이름없음.xlsx'
names_list = ['Name', 'January', 'February', 'March', 'April', 'May', 'June']
df = pd.read_excel(excel_file, header=None, names=names_list)
print("- pd.read_excel(excel_file, header=None, names=names_list):\n{0}".format(df))

excel_file = folder + '사원별_월간_판매현황.xlsx'
names_list = ['사원명', '1월', '2월', '3월', '4월', '5월', '6월']
# header=None은 열이름 행이 없다는 것이고, header=0은 열이름 행이 첫행이라는 것으로 첫행을 names_list 항목을 대체하라는 뜻
df = pd.read_excel(excel_file, header=0, names=names_list)
print("- pd.read_excel(excel_file, header=0, names=names_list):\n{0}".format(df))

# to_excel()을 이용해 DataFrame 데이터를 엑셀 파일로 쓰는 방법
print('-- to_excel()을 이용해 DataFrame 데이터를 엑셀 파일로 쓰는 방법')

excel_file = folder + '사원별_월간_판매현황2.xlsx'
df1 = pd.read_excel(excel_file, sheet_name=0)
df2 = pd.read_excel(excel_file, sheet_name=1)

excel_file = folder + '사원별_월간_판매현황_output.xlsx'
# index=False는 index를 포함하지 않게 하는 옵션
print("df1.to_excel(excel_file, sheet_name='상반기', index=False):\n{0}".format(df1.to_excel(excel_file, sheet_name='상반기', index=False)))
print("생성한 엑셀 파일: ", excel_file)

# DataFrame 데이터를 엑셀 파일의 '상반기'와 '하반기' 시트에 쓰기
print('-- 하나의 엑셀 파일에 여러 개의 DataFrame 데이터를 쓰려면 ExcelWriter로부터 객체를 생성해 to_excel()을 이용')
with pd.ExcelWriter(excel_file, engine='xlsxwriter') as excel_writer:
    df1.to_excel(excel_writer, sheet_name='상반기', index=False)
    df2.to_excel(excel_writer, sheet_name='하반기', index=False)

print("with pd.ExcelWriter(excel_file, engine='xlsxwriter') as excel_writer:"
      "\n\tdf1.to_excel(excel_writer, sheet_name='상반기', index=False)"
      "\n\tdf2.to_excel(excel_writer, sheet_name='하반기', index=False)")

# 여러 개의 DataFrame 데이터를 하나의 엑셀 워크시트에 위치를 지정해 쓰는 예
df1 = pd.DataFrame({'제품ID': ['P1001','P1002','P1003','P1004'],
                   '판매가격': [5000, 7000, 8000, 10000],
                   '판매량': [50, 93, 70, 48]})
df2 = pd.DataFrame({'제품ID': ['P2001','P2002','P2003','P2004'],
                   '판매가격': [5000, 7000, 8000, 10000],
                   '판매량': [50, 93, 70, 48]})
df3 = pd.DataFrame({'제품ID': ['P3001','P3002','P3003','P3004'],
                   '판매가격': [5000, 7000, 8000, 10000],
                   '판매량': [50, 93, 70, 48]})
df4 = pd.DataFrame({'제품ID': ['P4001','P4002','P4003','P4004'],
                   '판매가격': [5000, 7000, 8000, 10000],
                   '판매량': [50, 93, 70, 48]})

excel_file = folder + 'product_sales_in_one_worksheet.xlsx'
# 생성한 객체(excel_writer)을 이용해 DataFrame 데이터(df)를 쓰기
excel_writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')

# 여러 DataFrame 데이터를 하나의 엑셀 워크시트에 위치를 달리해서 출력
df1.to_excel(excel_writer)  # startrow=0, startcol=0과 동일
df2.to_excel(excel_writer, startrow=0, startcol=5, index=False)
df3.to_excel(excel_writer, startrow=6, startcol=0)
df4.to_excel(excel_writer, startrow=5, startcol=5, index=False, header=False)

print("\n-- 여러 DataFrame 데이터를 하나의 엑셀 워크시트에 위치를 달리해서 출력")
print("df1.to_excel(excel_writer)")
print("df2.to_excel(excel_writer, startrow=0, startcol=5, index=False)")
print("df3.to_excel(excel_writer, startrow=6, startcol=0)")
print("df4.to_excel(excel_writer, startrow=5, startcol=5, index=False, header=False)")

# [CSV 파일 읽고 엑셀 파일로 쓰기, 엑셀 파일 읽고 CSV 파일로 쓰기]
input_csv_file = folder + 'korea_rain1.csv'
output_excel_file = folder + 'out_korea_rain1.xlsx'

df = pd.read_csv(input_csv_file)
df.to_excel(output_excel_file, index=False)
print('\n- CSV 파일을 엑셀 파일로 변환하는 코드')
print('df = pd.read_csv(in_csv_file)')
print('df.to_excel(out_excel_file, index=False)')
print("출력 엑셀 파일:", output_excel_file)

# [엑셀 파일을 CSV 파일로 변환하는 코드]
input_excel_file = folder + 'korea_rain1.xlsx'
output_csv_file = folder + 'out_korea_rain_cp949.csv'

df = pd.read_excel(input_excel_file)
df.to_csv(output_csv_file, encoding='cp949', index=False)
print('\n- 엑셀 파일을 CSV 파일로 변환하는 코드')
print('df = pd.read_excel(input_excel_file)')
print("df.to_csv(output_csv_file, encoding='cp949',index=False)")
print("출력 CSV 파일:", output_csv_file)


