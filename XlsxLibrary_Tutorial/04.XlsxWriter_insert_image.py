"""
엑셀의 특정 셀에 그림을 삽입하려면 insert_image()를 이용

worksheet.insert_image(row, col, image_file[, options])
worksheet.insert_image(cell_address, image_file[, options])
"""
from datetime import datetime

import xlsxwriter


folder = './data/ch06/'
excel_file = folder + 'XlsxWriter_insert_image_01.xlsx'
image_file = './figures/book_image.png'

workbook = xlsxwriter.Workbook(excel_file)
worksheet = workbook.add_worksheet()

worksheet.set_column(0, 0, 35)

worksheet.write(1, 0, "그림 삽입(옵션 지정 없음):")
worksheet.insert_image(1, 1, image_file)

worksheet.write(8, 0, "그림 삽입(가로와 세로 위치 오프셋 조정):")
worksheet.write(9, 0, "{'x_offset': 25, 'y_offset': 10}")
worksheet.insert_image(8, 1, image_file, {'x_offset': 25, 'y_offset': 10})

worksheet.write(15, 0, "그림 삽입(크기 화대):")
worksheet.write(16, 0, "{'x_scale': 1.5, 'y_scale': 1.5}")
worksheet.insert_image(15, 1, image_file, {'x_scale': 1.5, 'y_scale': 1.5})

worksheet.write(25, 0, "그림 삽입(크기 화대):")
worksheet.write(26, 0, "{'x_scale': 0.75, 'y_scale': 0.7}")
worksheet.insert_image(25, 1, image_file, {'x_scale': 0.75, 'y_scale': 0.7})

workbook.close()

print("생성한 엑셀 파일:", excel_file)



"""
셀에 텍스트 상자를 삽입

worksheet.insert_textbox(row, col, text[, options])
worksheet.insert_textbox(cell_address, text[, options])
"""
folder = './data/ch06/'
excel_file = folder + 'XlsxWriter_insert_textbox_01.xlsx'

workbook = xlsxwriter.Workbook(excel_file)
worksheet = workbook.add_worksheet()

worksheet.set_column(0, 0, 40)
text = "텍스트 상자"

worksheet.write(1, 0, "텍스트 상자 삽입(옵션 지정 없음):")
worksheet.insert_textbox(1, 1, text)

worksheet.write(8, 0, "텍스트 상자 삽입(가로와 세로 위치 오프셋 조정):")
worksheet.write(9, 0, "{'x_offset': 25, 'y_offset': 10}")
worksheet.write(10, 0, "'width': 240, 'height': 100'")

options = {'x_offset': 25, 'y_offset': 10, 'width': 240, 'height': 100}
worksheet.insert_textbox(8, 1, text, options)

worksheet.write(16, 0, "텍스트 상자 삽입(글꼴, 맞춤 속성 지정):")
worksheet.write(17, 0, "{'align': {'vertical': 'middle', 'horizontal': 'center'},")
worksheet.write(18, 0, "'font': {'bold': True, 'size': 15")

options = {'align': {'vertical': 'middle', 'horizontal': 'center'},
           'font': {'bold': True, 'size': 15}}
worksheet.insert_textbox(16, 1, text, options)

worksheet.write(23, 0, "텍스트 상자 삽입(테두리, 채우기 속성 지정):")
worksheet.write(24, 0, "{'border': {'color': 'black', 'width': 2},")
worksheet.write(25, 0, "'fill': {'color': 'yellow'}")

options = {'border': {'color': 'black', 'width': 2},
           'fill': {'color': 'yellow'}}
worksheet.insert_textbox(23, 1, text, options)

workbook.close()

print("생성한 엑셀 파일:", excel_file)



