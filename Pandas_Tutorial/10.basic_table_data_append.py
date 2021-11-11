"""
판다스에는 Sereis 데이터나 DataFrame 데이터에 새로운 데이터를 세로 방향(index 증가 방향)으로 합하려면 append()를 이용
"""
import pandas as pd
import numpy as np

# 세로나 가로 방향으로 연결: concat()
s1 = pd.Series([10, 20, 30])
print("s1=\n{0}".format(s1))
s2 = pd.Series([40, 50, 60])
print("\ns2=\n{0}".format(s2))
s3 = pd.Series([70, 80, 90])
print("\ns3=\n{0}".format(s3))

# 세로 방향으로 연결
print("\n- s1에 s2를 세로 방향으로 연결하되 기존 index를 무시하고 새로운 index를 생성")
print("s1.append(s2, ignore_index=True)=\n{0}".format(s1.append(s2, ignore_index=True)))

print("\n- s1에 s2, s3를 세로 방향으로 연결하되 기존 index를 무시하고 새로운 index를 생성")
print("s1.append([s2, s3], ignore_index=True)=\n{0}".format(s1.append([s2, s3], ignore_index=True)))

df1 = pd.DataFrame({'물리': [95, 92, 98, 100],
                    '화학': [91, 93, 97, 99]})
print("\ndf1=\n{0}".format(df1))

df2 = pd.DataFrame({'물리': [87, 89],
                    '화학': [85, 90]})
print("\ndf2=\n{0}".format(df2))

df3 = pd.DataFrame({'물리': [72, 85]})
print("\ndf3=\n{0}".format(df3))

df4 = pd.DataFrame({'생명과학': [94, 91, 94, 83],
                    '지구과학': [86, 94, 89, 93]})
print("\ndf4=\n{0}".format(df4))

print("\n- df2에 df3를 세로 방향으로 연결하되 기존 index를 무시하고 새로운 inde를 생성")
print("df2.append(df3, ignore_index=True)=\n{0}".format(df2.append(df3, ignore_index=True)))

print("\n- df2에 df3를 세로 방향으로 연결하되 기존 index를 무시하고 새로운 inde를 생성")
print("df2.append(df1.append([df2, df3], ignore_index=True)=\n{0}".format(df1.append([df2, df3], ignore_index=True)))

# 가로방향(index 기준)으로 병합: join()
print("\n[ 가로방향(index 기준)으로 병합: join() ]")
dict_data = {'A': ['a0', 'a1', 'a2'],
             'B': ['b0', 'b1', 'b2']}

df_left1 = pd.DataFrame(dict_data)
print('df_left1=\n{0})'.format(df_left1))

dict_data = {'C': ['c0', 'c1', 'c2'],
             'D': ['d0', 'd1', 'd2']}

df_right1 = pd.DataFrame(dict_data, index=[1,2,3])
print('\ndf_right1=\n{0}'.format(df_right1))

dict_data = {'A': ['a0', 'a1', 'a2'],
             'B': ['d0', 'd1', 'd2']}

df_right2 = pd.DataFrame(dict_data)
print('\ndf_right2=\n{0}'.format(df_right2))

# 가로방향(index 기준)으로 병합: join()
print("\n[ 가로방향(index 기준)으로 병합: join() ]")
print("- 왼쪽 데이터는 모두 선택, 왼쪽 index와 연관된 항목이 있는 오른쪽 데이터만 병합 (how='left')")
df_left1.join(df_right1, how='left')     # df_left1.join(df_right1) 과 동일
print("df_left1.join(df_right1, how='left')=\n{0}".format(
    df_left1.join(df_right1, how='left')
))

print("\n- 오른쪽 데이터는 모두 선택, 오른쪽 index와 연관된 항목이 있는 왼쪽 데이터만 병합 (how='right')")
df_left1.join(df_right1, how='left')     # df_left1.join(df_right1) 과 동일
print("df_left1.join(df_right1, how='right')=\n{0}".format(
    df_left1.join(df_right1, how='right')
))

print("\n- index를 기준으로 왼쪽, 오른쪽 열 데이터를 모두 병합 (how='outer')")
df_left1.join(df_right1, how='outer')     # df_left1.join(df_right1) 과 동일
print("df_left1.join(df_right1, how='outer')=\n{0}".format(
    df_left1.join(df_right1, how='outer')
))

print("\n- index를 기준으로 왼쪽, 오른쪽에 연관된 항목이 모두 있는 데이터를 모두 병합 (how='inner')")
df_left1.join(df_right1, how='inner')     # df_left1.join(df_right1) 과 동일
print("df_left1.join(df_right1, how='inner')=\n{0}".format(
    df_left1.join(df_right1, how='inner')
))


# 가로 방향(열 기준)으로 병합: merge()
# DataFrame 데이터끼리 열을 기준으로 가로 방향(columns 증가 방향)으로 병합하려면 merge() 이용
print("\n[ 가로 방향(열 기준)으로 병합: merge() ]")

df_left3 = pd.DataFrame({'key': ['k0', 'k1', 'k2', 'k3'],
                         'A': ['a0', 'a1', 'a2', 'a3']})
print("\n- df_left3=\n{0}".format(df_left3))

df_right3 = pd.DataFrame({'key': ['k2', 'k3', 'k4', 'k5'],
                          'B': ['b2', 'b3', 'b4', 'b5']})
print("\n- df_right3=\n{0}".format(df_right3))

print("\n- df_left3.merge(df_right3, how='left', on='key')=\n{0}".format(
    df_left3.merge(df_right3, how='left', on='key')
))

print("\n- df_left3.merge(df_right3, how='right', on='key')=\n{0}".format(
    df_left3.merge(df_right3, how='right', on='key')
))

print("\n- df_left3.merge(df_right3, how='outer', on='key')=\n{0}".format(
    df_left3.merge(df_right3, how='outer', on='key')
))

print("\n- df_left3.merge(df_right3, how='inner', on='key')=\n{0}".format(
    df_left3.merge(df_right3, how='inner', on='key')
))

df_left4 = pd.DataFrame({'key': ['k0', 'k1', 'k2', 'k3'],
                         'A': ['a0', 'a1', 'a2', 'a3'],
                         'C': ['c0', 'c1', 'c2', 'c3']})
print("\n- df_left4=\n{0}".format(df_left4))

df_right4 = pd.DataFrame({'key': ['k0', 'k1', 'k2', 'k3'],
                         'A': ['a0', 'a1', 'a4', 'a5'],
                         'D': ['d0', 'd1', 'd2', 'd3']})
print("\n- df_right4=\n{0}".format(df_right4))

print("\n- df_left4.merge(df_right4, how='inner')=\n{0}".format(
    df_left4.merge(df_right4, how='inner')
))

print("\n- df_left4.merge(df_right4, how='inner', on=['key', 'A'])=\n{0}".format(
    df_left4.merge(df_right4, how='inner', on=['key', 'A'])
))

print("\n- df_left4.merge(df_right4, how='outer', on='key')=\n{0}".format(
    df_left4.merge(df_right4, how='outer', on='key')
))

print("\n- df_left4.merge(df_right4, how='outer', on='key', suffixes=('_left', '_right'))=\n{0}".format(
    df_left4.merge(df_right4, how='inner', on='key', suffixes=('_left', '_right'))
))

df_left5 = pd.DataFrame({'key_left': ['k0', 'k1', 'k2', 'k3'],
                         'A': ['a0', 'a1', 'a2', 'a3']})
print('\ndf_left5=\n{0}'.format(df_left5))

df_right5 = pd.DataFrame({'key_right': ['k1', 'k2', 'k3'],
                          'A': ['a1', 'a4', 'a5']}, index=[2,3,4])
print('\ndf_right5=\n{0}'.format(df_right5))

print("\n- 두 개의 DataFrame 데이터를 통합")
print("df_left5.merge(df_right5, how='left', left_on='key_left', right_on='key_right')=\n{0}".format(
    df_left5.merge(df_right5, how='left', left_on='key_left', right_on='key_right')
))

code_list=['LS05', 'SM10', 'BP70', 'LS10', 'BP70', 'SM10', 'LS05']
sales_list = [29, 25, 30, 22, 19, 38, 45]
store_list = ['강남', '강남', '강남', '대학로', '대학로', '인천공항', '인천공항']

# 제품의 코드와 매장별 판매량이 있는 DataFrame 데이터 생성
df_sales = pd.DataFrame({'code': code_list,
                         'sales': sales_list,
                         'store': store_list})
print("df_sales=\n{0}".format(df_sales))

print("\n- 제품의 코드와 제품 이름이 있는 DataFrame 데이터 생성")
df_ref = pd.DataFrame({'code': ['LS05', 'SM10', 'BP70','LS10'],
                       'name': ['브리오슈', '베이글', '치아바타', '바게트']})
print("df_ref=\n{0}".format(df_ref))

df_sales.merge(df_ref, how='left', on='code')
print("\ndf_sales.merge(df_ref, how='left', on='code')=\n{0}".format(df_sales.merge(df_ref, how='left', on='code')))
