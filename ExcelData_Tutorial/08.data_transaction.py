"""
임의의 데이터 구조를 갖는 엑셀 파일에서 원하는 데이터를 출출해 원본 데이터와는 다른 구조로 데이터를 정리하는 과정을 살펴봅니다.
"""
from pathlib import Path

import pandas as pd


def excel_data_extractor(excel_file, row_num):
    df = pd.read_excel(excel_file)

    # 특정 위치의 값 추출 후 리스트 생성
    column_names0 = [df.iloc[7][0], df.iloc[7][2], df.iloc[0][0]]
    column_names1 = list(df.iloc[11, 1:6].values)

    column_names = column_names0 + column_names1
    # print(column_names0)
    # print(column_names1)
    # print(column_names)

    df_new = pd.DataFrame(columns=column_names)
    date = df.iloc[8][0]
    date_new = date.strftime('%Y-%m-%d')
    issue_num = df.iloc[8][2]
    company = df.iloc[0][1]

    # row_num = 6     # 추출한 DataFrame의 열 개수
    df_new[column_names[0]] = [date_new] * row_num
    df_new[column_names[1]] = [issue_num] * row_num
    df_new[column_names[2]] = [company] * row_num
    # print(df_new)

    # df_new[column_names[3]] = df.iloc[12:12+row_num, 1].values
    # print(df_new)

    for k in range(5):
        df_new[column_names[3+k]] = df.iloc[12:12+row_num, 1+k].values
    # print(df_new)

    df_new = df_new.dropna()    # NaN이 들어간 데이터 제거
    # print(df_new)

    return df_new


folder = './data/ch07/transaction/raw/'
excel_file = folder + '거래명세서_No_1258115.xlsx'

df1 = excel_data_extractor(excel_file, 6)
# print(df1)

raw_data_dir = Path(folder)

excel_files = raw_data_dir.glob('거래명세서_No*.xlsx')

total_df = pd.DataFrame()

for excel_file in excel_files:
    df = excel_data_extractor(excel_file, 6)
    total_df = total_df.append(df, ignore_index=True)

print(total_df)

folder = './data/ch07/transaction/'
merged_excel_file = folder + '거래명세서_데이터_추출_후_통합.xlsx'

total_df.to_excel(merged_excel_file, index=False)

print("생성 파일:", merged_excel_file)
