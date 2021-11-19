"""
판다스의 to_excel() 은 셀 서식 지정(배경색, 글꼴, 테두리 등)을 할 수 없다.
XlsxWriter는 엑셀 파일 자체의 파일 포맷을 분석해 읽고 쓰므로 윈도우, 맥, 리눅스에서 모두 사용할 수 있다.
하지만 보안 프로그램이 설치된 컴퓨터에서는 엑셀 파일을 읽지 못할 수 있으며,
엑셀과 상호 작용이 없습니다. 따라서 실시간으로 확인할 수 없으며, 코드 수행이 끝난 후에 결과를 확인할 수 있습니다.
https://xlsxwriter.readthedocs.io

Workbook : 문서 전체
Worksheet : 행과 열의 번호로 위치를 지정할 수 있는 2차원 셀

workbook = xlsxwriter.Workbook(excel_file)
worksheet = workbook.add_worksheet([worksheet_name])
worksheet.write(row, col, cell_data)
worksheet.write(cell_address, cell_data)
"""

import xlsxwriter

folder = './data/ch06/'
excel_file = folder + 'XlsxWriter_start_01.xlsx'

workbook = xlsxwriter.Workbook(excel_file)
worksheet = workbook.add_worksheet()
worksheet.write(0, 0, 100)
worksheet.write(1, 0, 3.14)
worksheet.write(2, 0, '안녕')
worksheet.write(3, 0, '=COS(PI()/4)')
worksheet.write(4, 0, '')
worksheet.write(5, 0, None)

worksheet.write('B1', '←숫자(정수) 입력')
worksheet.write('B2', '←숫자(실수) 입력')
worksheet.write('B3', '←문자열 입력')
worksheet.write('B4', '←엑셀 함수 계산 입력')
worksheet.write('B5', '←빈 문자로 공백 입력')
worksheet.write('B6', '←None으로 공백 입력')

workbook.close()

print("생성한 엑셀 파일:", excel_file)


""" 
엑셀 함수로 합계와 평균을 구하기
"""
folder = './data/ch06/'
excel_file = folder + 'XlsxWriter_start_03.xlsx'

workbook = xlsxwriter.Workbook(excel_file)
worksheet = workbook.add_worksheet()

worksheet.write('A1', '지점1')
worksheet.write('A2', '지점2')
worksheet.write('A3', '지점3')
worksheet.write('A4', '지점4')
worksheet.write('A5', '합계')
worksheet.write('A6', '평균')
worksheet.write('B1', 10)
worksheet.write('B2', 15)
worksheet.write('B3', 12)
worksheet.write('B4', 9)
worksheet.write('B5', '=SUM(B1:B4)')
worksheet.write('B6', '=AVERAGE(B1:B4)')

workbook.close()

print("생성한 엑셀 파일:", excel_file)

