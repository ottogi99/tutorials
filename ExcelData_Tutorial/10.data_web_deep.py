"""
네이버 뮤직에서 국내 가요 순위를 주차별로 가져와서 엑셀 파일로 저장하는 방법을 알아봅니다.
"""
from pathlib import Path

import pandas as pd


def naver_music_top100(year, month, week):
    base_url = 'https://music.naver.com/listen/history/index.nhn?type=DOMESTIC_V2'
    df_top100 = pd.DataFrame()

    for page in pages:
        url = base_url + '&year={0}&month={1}}&week={2}&page={3}'.format(year, month, week, page)

        # 2021-11-22 일 기준 "No tables found" 발생(홈페이지 개편된 듯)
        dfs = pd.read_html(url)

        df_top100 = df_top100.append(dfs[0][['순위', '곡명', '아티스트']])

    return df_top100


df = naver_music_top100(2019, 12, 1)

folder = './data/ch07/webpage_data/'
excel_file = folder + '네이버_뮤직_Top100.xlsx'

dfs[0].to_excel(excel_file, index=False)
print("생성 파일:", excel_file)
