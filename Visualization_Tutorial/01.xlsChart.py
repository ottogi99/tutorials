"""
파이썬에서 엑셀 라이브러리를 이용하면 엑셀의 차트를 생성할 수 있습니다.
"""
import pandas as pd

"""
- 막대형 차트
"""
folder = './data/ch08/'
excel_file = folder + '영업팀별_판매현황.xlsx'

df = pd.read_excel(excel_file)

folder = './data/ch08/'
excel_file_chart = folder + '영업팀별_판매현황_세로막대형차트.xlsx'

excel_writer = pd.ExcelWriter(excel_file_chart, engine='xlsxwriter')

worksheet_name = 'Sheet1'
df.to_excel(excel_writer, sheet_name=worksheet_name, index=False)

workbook = excel_writer.book
worksheet = excel_writer.sheets[worksheet_name]

chart = workbook.add_chart({'type': 'column'})
# # 막대형 차트 데이터 범위 지정
# chart.add_series({'values': '=Sheet1!B2:B7'})
# chart.add_series({'values': '=Sheet1!C2:C7'})
# chart.add_series({'values': '=Sheet1!D2:D7'})

columns_len = len(df.columns)

for k in range(columns_len - 1):
    start_row = 1
    start_column = k + 1
    end_row = len(df.index)
    end_column = k + 1
    
    chart.add_series({
        'values': [worksheet_name, start_row, start_column, end_row, end_column],   # 막대형 차트를 위한 데이터 범위 지정
        'categories': [worksheet_name, start_row, 0, end_row, 0],   # 축 값에 사용할 데이터 범위 지정
        'name': [worksheet_name, 0, k+1],   # 범례 이름을 사용할 데이터 지정
        'overlap': -15      # 그래프 사이의 간격 지정
    })

chart.set_title({'name': '영업팀별 하반기 판매현황'})
chart.set_x_axis({'name': '월'})
chart.set_y_axis({'name': '판매현황'})

worksheet.insert_chart(1, columns_len, chart, {'x_offset': 25, 'y_offset': 10})
# worksheet.insert_chart('E2', chart, {'x_offset': 25, 'y_offset': 10})

excel_writer.save()

print("생성 파일:", excel_file_chart)
