import glob
import os.path

import numpy as np
import pandas as pd
from os import path
import math

# # CSV(dat) 파일 목록 가져오기
# target_dir = './imha_data'
# target_wildcard = '*.dat'
# target_path = os.path.join(target_dir, target_wildcard)
#
# dfs = []
# for path in glob.iglob(target_path):
#     if os.path.exists(path):
#         print(os.path.abspath(path))
#         # df = pd.read_csv(path)
#         df = pd.read_csv(path, header=None, skiprows=1, nrows=1)
#         names = df.values[0]
#         df = pd.read_csv(path, header=None, names=names, skiprows=4)
#         dfs.append((os.path.basename(path), df))
#
# # CSV 파일을 EXCEL로 저장
# output_path = './imha_data_output.xlsx'
# with pd.ExcelWriter(output_path, engine='xlsxwriter') as excel_writer:
#     for path, df in dfs:
#         df.to_excel(excel_writer, sheet_name=path, index=False)

# # CSV(dat) 파일 목록 가져오기
# target_dir = './imha_data'
# target_wildcard = 'FBG_20211108_DATA.csv'
# target_path = os.path.join(target_dir, target_wildcard)
#
# dfs = []
# for path in glob.iglob(target_path):
#     if os.path.exists(path):
#         print(os.path.abspath(path))
#         # df = pd.read_csv(path)
#         df = pd.read_csv(path, header=0)
#         dfs.append((os.path.basename(path), df))

# CSV(dat) 파일 목록 가져오기
target_dir = './imha_data'
target_wildcard = 'FBG_20211108_DATA2.csv'
target_path = os.path.join(target_dir, target_wildcard)

dfs = []
for path in glob.iglob(target_path):
    if os.path.exists(path):
        print(os.path.abspath(path))
        # df = pd.read_csv(path)
        df = pd.read_csv(path)
        dfs.append((os.path.basename(path), df))

# CSV 파일을 EXCEL로 저장
output_path = './imha_fbg_data2_output.xlsx'
with pd.ExcelWriter(output_path, engine='xlsxwriter') as excel_writer:
    for path, df in dfs:
        df.to_excel(excel_writer, sheet_name=path, index=False)


# # EXCEL 파일 목록 가져오기
# target_dir = './imha_data'
# target_wildcard = '*.xlsx'
# target_path = os.path.join(target_dir, target_wildcard)
#
# dfs = []
# for path in glob.iglob(target_path):
#     if os.path.exists(path):
#         print(os.path.abspath(path))
#         df = pd.read_excel(path, header=None, skiprows=1, nrows=1)
#         names = df.values[0]
#         df = pd.read_excel(path, header=None, names=names, skiprows=4)
#         dfs.append((os.path.basename(path), df))
#
# output_path = './imha_data_output.xlsx'
# with pd.ExcelWriter(output_path, engine='xlsxwriter') as excel_writer:
#     for path, df in dfs:
#         df.to_excel(excel_writer, sheet_name=path, index=False)

# limha_2_limha.dat 과 limha_2_Andong_Imha.dat JOIN
# patha = './imha_data/limha_2_limha.dat'
# pathb = './imha_data/limha_2_Andong_Imha.dat'

# # CR1000 테스트
# # 1)번 테스트
# patha = './imha_data/limha_2_limha.dat'
# # 2)번 테스트
# # patha = './imha_data/limha_1_limha.dat'
# # 3)번 테스트
# patha = './imha_data/limha_2_Andong_Imha.dat'
# pathb = './imha_data/202103251000_DATA.xlsx'

# 광로거 테스트
# patha = './imha_data/FBG_20211108_DATA.txt'
patha = './imha_data/FBG_20211108_DATA2.txt'
pathb = './imha_data/20211108_DATA.xlsx'

# 광로거
dfa = pd.read_csv(patha, header=0, sep='\t')

# CR1000
# # dfa = pd.read_csv(patha, header=0)
# dfa = pd.read_csv(patha, header=None, skiprows=1, nrows=1)
# names = dfa.values[0]
# dfa = pd.read_csv(patha, header=None, names=names, skiprows=4)


# CR1000
# # dfa = pd.read_csv(patha, header=0)
# dfa = pd.read_csv(patha, header=None, skiprows=1, nrows=1)
# names = dfa.values[0]
# dfa = pd.read_csv(patha, header=None, names=names, skiprows=4)

# dfb = pd.read_csv(pathb, header=0)
# dfb = pd.read_csv(pathb, header=None, skiprows=1, nrows=1)
# names = dfb.values[0]
# dfb = pd.read_csv(pathb, header=None, names=names, skiprows=4)
dfb = pd.read_excel(pathb)#(pathb, header=None, names=names, skiprows=4)

# dfc = dfa.join(dfb, how='inner', on="TIMESTAMP")
# dfa['TIMESTAMP'] = dfa['TIMESTAMP'].astype(str)
# dfb['TIMESTAMP'] = dfb['TIMESTAMP'].astype(str)

# dfm = pd.concat([dfa, dfb], axis=1, join="inner")
# dfm.to_excel('./output_concat.xlsx', sheet_name='머지', index=False)

# dfc = dfa.merge(dfb, how='left', on="TIMESTAMP")
# dfc.to_excel('./output_merge.xlsx', sheet_name='머지', index=False)

# print(dfa.values[0])
# print(dfb)
dfa_values = dfa.values[0];
for dfa_i, v1 in enumerate(dfa_values):
    try:
        v1 = float(v1)
    except ValueError:
        continue

    v1 = round(v1, 3)
    # print("try find {0} item".format(v1))
    for i, db_row in enumerate(dfb.values):
        # print('i=', i)
        if v1 in db_row:
            print("find item: {0}".format(v1))

            matched_index = [j for j, v2 in enumerate(db_row) if str(v2) == str(v1)]
            print("DataFile> index={0} field={1}, value={2}".format(dfa_i, dfa.columns[dfa_i], v1))
            print("DbFile> index={0}, field={1}, sensor_id={2}".format(matched_index, dfb.columns[matched_index], dfb.values[i][2]))
            break

exit()


    # matched_index = [i for i, v2 in enumerate(dfb.values[0]) if str(v2) == str(v1)]
    # if matched_index:
    #     print("'{0}' 값과 {1} 의 필드값이 일치합니다.".format(v1, dfb.columns[matched_index]))

exit()

# # df = pd.read_csv(csv_file)
# df = pd.read_csv(input_file, header=None, skiprows=1, nrows=1)
# # print(df)
# names = df.values[0]
# # print(names)
#
# # df = pd.read_csv(csv_file, header=None, names=names, index_col=0, skiprows=4)
# df = pd.read_csv(input_file, header=None, names=names, skiprows=4)
# print(df)


# 필요한 데이터 분류



# Excel 파일 저장하기
output_file = path + 'out_korea_rain1.xlsx'
df.to_excel(output_file, index=False)
