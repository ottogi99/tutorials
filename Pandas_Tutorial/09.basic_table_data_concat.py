"""
판다스에는 Sereis 데이터나 DataFrame 데이터를 가로나 세로 방향으로 연결하거나 병합하기 위한 다양한 메서드가 있습니다.
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
print("\n- 세로 방향으로 연결")
print("pd.concat([s1, s2])=\n{0}".format(pd.concat([s1, s2])))
print("\n- 기존 index를 무시하고 새로운 index 생성")
print("pd.concat([s1, s2], ignore_index=True)=\n{0}".format(pd.concat([s1, s2], ignore_index=True)))
print("pd.concat([s1, s2, s3], ignore_index=True)=\n{0}".format(pd.concat([s1, s2, s3], ignore_index=True)))

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

print("\n- 세로 방향으로 연결하되 기존 index를 무시")
print("pd.concat([df1, df2], ignore_index=True)=\n{0}".format(pd.concat([df1, df2], ignore_index=True)))

print("\n- columns의 개수가 같지 않을때는 NaN으로 채움")
print("pd.concat([df2, df3], ignore_index=True)=\n{0}".format(pd.concat([df2, df3], ignore_index=True)))

print("\n- 공통으로 있는 데이터만 연결하려면 join='inner'")
print("pd.concat([df2, df3], ignore_index=True, join='inner')=\n{0}".format(
    pd.concat([df2, df3], ignore_index=True, join='inner')
))

print("\n- 가로방향으로 연결 (axis=1)")
print('pd.concat([df1, df4], axis=1)=\n{0}'.format(
    pd.concat([df1, df4], axis=1)
))

print("\n- index 개수가 같지 않을 때 가로방향으로 연결")
print("pd.concat([df2, df4], axis=1)=\n{0}".format(
    pd.concat([df2, df4], axis=1)
))

print("\n- 가로방향으로 공통 데이터만 연결")
print("pd.concat([df2, df4], axis=1, join='inner')=\n{0}".format(
    pd.concat([df2, df4], axis=1, join='inner')
))


