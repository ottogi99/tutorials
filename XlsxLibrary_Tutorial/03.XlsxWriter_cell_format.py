"""
XlsxWriter를 사용해 데이터를 쓸 때 셀 서식을 지정하는 방법

cell_format = workbook.add_format([props])

worksheet.write(row, col, cell_data, cell_format)
worksheet.write(cell_address, cell_data, cell_format)

"""
from datetime import datetime

import xlsxwriter

folder = './data/ch06/'
excel_file = folder + 'XlsxWriter_cell_format_01.xlsx'

workbook = xlsxwriter.Workbook(excel_file)
worksheet = workbook.add_worksheet()

cell_format = workbook.add_format({'font_name': '바탕',
                                   'bold': True,
                                   'font_color': 'blue'})

# 메서드를 이용해 서식 추가 지정
cell_format.set_italic()
cell_format.set_font_size(20)

worksheet.write('A1', '셀 서식 미지정')
worksheet.write('A2', '셀 서식 지정', cell_format)

workbook.close()

print("생성한 엑셀 파일:", excel_file)


""" 
채우기 관련 속성과 메서드
set_bg_color()
set_pattern()
set_fg_color()
"""
folder = './data/ch06/'
excel_file = folder + 'XlsxWriter_cell_format_02.xlsx'

workbook = xlsxwriter.Workbook(excel_file)
worksheet = workbook.add_worksheet()

cell_format1 = workbook.add_format()
cell_format2 = workbook.add_format()
cell_format3 = workbook.add_format()
cell_format4 = workbook.add_format()
cell_format5 = workbook.add_format()
cell_format6 = workbook.add_format()

cell_format1.set_bg_color('lime')

cell_format2.set_bg_color('blue')
cell_format2.set_font_color('white')

cell_format3.set_bg_color('red')
cell_format3.set_pattern(1)
cell_format3.set_font_color('white')

cell_format4.set_bg_color('red')
cell_format4.set_pattern(6)
cell_format4.set_font_color('white')

cell_format5.set_bg_color('yellow')
cell_format5.set_pattern(7)
cell_format5.set_font_color('brown')

cell_format6.set_bg_color('#FF6600')
cell_format6.set_pattern(18)
cell_format6.set_font_color('brown')

worksheet.write('B1', "안녕")
worksheet.write('B3', "안녕", cell_format1)
worksheet.write('B5', "안녕", cell_format2)
worksheet.write('B7', "안녕", cell_format3)
worksheet.write('D3', "안녕", cell_format4)
worksheet.write('D5', "안녕", cell_format5)
worksheet.write('D7', "안녕", cell_format6)

workbook.close()

print("생성한 엑셀 파일:", excel_file)

""" 
3. 테두리 관련 속성과 메서드
    set_border()
    set_bottom()    set_top()   set_left()  set_right()
    set_border_color()  set_bottom_color()  set_top_color() set_left_color  set_right_color()
"""
folder = './data/ch06/'
excel_file = folder + 'XlsxWriter_cell_format_03.xlsx'

workbook = xlsxwriter.Workbook(excel_file)
worksheet = workbook.add_worksheet()

cell_format1 = workbook.add_format()
cell_format2 = workbook.add_format()
cell_format3 = workbook.add_format()
cell_format4 = workbook.add_format()
cell_format5 = workbook.add_format()
cell_format6 = workbook.add_format()

cell_format1.set_border(1)
cell_format2.set_border(2)
cell_format2.set_border_color('blue')
cell_format3.set_bottom(8)
cell_format4.set_left(2)
cell_format5.set_right(5)
cell_format6.set_border(6)

worksheet.write('B1', "안녕")
worksheet.write('B3', "안녕", cell_format1)
worksheet.write('B5', "안녕", cell_format2)
worksheet.write('B7', "안녕", cell_format3)
worksheet.write('D3', "안녕", cell_format4)
worksheet.write('D5', "안녕", cell_format5)
worksheet.write('D7', "안녕", cell_format6)

workbook.close()

print("생성한 엑셀 파일:", excel_file)

""" 
4. 숫자 형식 관련 속성과 메서드
    set_num_format()
"""
folder = './data/ch06/'
excel_file = folder + 'XlsxWriter_cell_format_04.xlsx'

workbook = xlsxwriter.Workbook(excel_file)
worksheet = workbook.add_worksheet()

cell_format_border = workbook.add_format()
cell_format_border.set_border(1)

# cell_formats = [workbook.add_format() for k in range(8)]
cell_formats = [workbook.add_format() for k in range(13)]

for k in range(13):
    cell_formats[k].set_num_format(k+1)

num_data1 = 1234.567
num_data2 = -1234.567

worksheet.write('A1', "입력", cell_format_border)
worksheet.write('B1', num_data1, cell_format_border)
worksheet.write('C1', num_data2, cell_format_border)

worksheet.write('A3', "인덱스")
worksheet.write('B3', "서식 지정 출력 결과")
worksheet.write('C3', "서식 지정 출력 결과")

for k in range(8):
    row = k + 3
    index = k + 1
    worksheet.write(row, 0, index)
    worksheet.write(row, 1, num_data1, cell_formats[k])
    worksheet.write(row, 2, num_data2, cell_formats[k])

num_data = [0.98765, 0.98765, 3000000000, 18.25, 20.39]
worksheet.write(12, 0, "인덱스")
worksheet.write(12, 1, "입력한 숫자")
worksheet.write(12, 2, "서식지정 출력 결과")

for k, value in enumerate(num_data):
    index = k + 12
    worksheet.write(index + 1, 0, index)
    worksheet.write(index + 1, 1, value)
    worksheet.write(index + 1, 2, value, cell_formats[8+k])

workbook.close()

print("생성한 엑셀 파일:", excel_file)

""" 
5. 날짜와 시각의 서식을 지정하는 예
"""
folder = './data/ch06/'
excel_file = folder + 'XlsxWriter_cell_format_06.xlsx'

workbook = xlsxwriter.Workbook(excel_file)
worksheet = workbook.add_worksheet()

datetime_formats = ['m/d/yy',
                    'd-mmm-yyy',
                    'd-mmm',
                    'mmm-yy',
                    'h:mm AM/PM',
                    'h:mm:ss AM/PM',
                    'h:mm',
                    'h:mm:ss',
                    'm/d/yy h:mm',
                    'yyyy"년" mm"월" dd"일"',
                    'yyyy"년" mm"월" dd"일" hh:mm:ss',
                    'yy"년" m"월" d"일"',
                    'yy"년" m"월" d"일" hh:mm:ss',
                    ]

cell_formats = [workbook.add_format() for k in range(0, len(datetime_formats))]

for k in range(0, len(datetime_formats)):
    if (k < 9):
        cell_formats[k].set_num_format(k+14)
    else:
        cell_formats[k].set_num_format(datetime_formats[k])

cell_format = workbook.add_format({'bold': True})

datetime_data = datetime(2021, 4, 8, 17, 38, 59)

worksheet.write(0, 0, "인덱스", cell_format)
worksheet.write(0, 1, "서식 지정 문자열", cell_format)
worksheet.write(0, 2, "서식 지정 출력 결과", cell_format)

for k in range(0, len(datetime_formats)):
    index = k + 14
    row = k + 1
    if (k < 9):
        worksheet.write(row, 0, index)
    else:
        worksheet.write(row, 0, "한글로 날짜 서식 지정")

    worksheet.write(row, 1, datetime_formats[k])
    worksheet.write(row, 2, datetime_data, cell_formats[k])

workbook.close()

print("생성한 엑셀 파일:", excel_file)

""" 
6. 맞춤 관련 속성과 메서드
    set_align()     set_indent()    set_rotation()
    set_text_wrap() set_shrink()    set_center_across()
    set_reading_order()
"""
folder = './data/ch06/'
excel_file = folder + 'XlsxWriter_cell_format_07.xlsx'

workbook = xlsxwriter.Workbook(excel_file)
worksheet = workbook.add_worksheet()

cell_format1 = workbook.add_format({'align': 'left'})
cell_format2 = workbook.add_format({'align': 'center'})
cell_format3 = workbook.add_format({'align': 'right'})

cell_format4 = workbook.add_format({'valign': 'top'})
cell_format5 = workbook.add_format({'valign': 'vcenter'})
cell_format6 = workbook.add_format({'valign': 'bottom'})

cell_format7 = workbook.add_format({'align': 'center', 'valign': 'vcenter'})

worksheet.write('A1', "텍스트 맞춤(서식 지정 없음)")
worksheet.write('A2', "텍스트 맞춤(가로 맞춤: 왼쪽)", cell_format1)
worksheet.write('A3', "텍스트 맞춤(가로 맞춤: 가운데)", cell_format2)
worksheet.write('A4', "텍스트 맞춤(가로 맞춤: 오른쪽)", cell_format3)
worksheet.write('A5', "텍스트 맞춤(가로 맞춤: 위쪽)", cell_format4)
worksheet.write('A6', "텍스트 맞춤(가로 맞춤: 가운데)", cell_format5)
worksheet.write('A7', "텍스트 맞춤(가로 맞춤: 아래쪽)", cell_format6)
worksheet.write('A8', "텍스트 맞춤(가로: 가운데 + 세로: 가운데)", cell_format7)

workbook.close()

print("생성한 엑셀 파일:", excel_file)

""" 
7. 행과 열의 높이와 너비 지정
worksheet.set_row(row, height[, cell_format])
worksheet.set_column(first_col, last_col, width[, cell_format])
"""

folder = './data/ch06/'
excel_file = folder + 'XlsxWriter_cell_format_08.xlsx'

workbook = xlsxwriter.Workbook(excel_file)
worksheet = workbook.add_worksheet()

worksheet.set_row(0, 20)
worksheet.set_row(1, 40)
worksheet.set_row(2, 60)

worksheet.set_column(0, 0, 15)
worksheet.set_column(1, 2, 20)
worksheet.set_column(3, 3, 25)

worksheet.write('A1', "높이:20, 너비:15")
worksheet.write('A2', "높이:40, 너비:15")
worksheet.write('A3', "높이:60, 너비:15")

worksheet.write('B1', "높이:20, 너비:20")
worksheet.write('B2', "높이:40, 너비:20")
worksheet.write('B3', "높이:60, 너비:20")

worksheet.write('C1', "높이:20, 너비:20")
worksheet.write('C2', "높이:40, 너비:20")
worksheet.write('C3', "높이:60, 너비:20")

worksheet.write('D1', "높이:20, 너비:25")
worksheet.write('D2', "높이:40, 너비:25")
worksheet.write('D3', "높이:60, 너비:25")

workbook.close()

print("생성한 엑셀 파일:", excel_file)