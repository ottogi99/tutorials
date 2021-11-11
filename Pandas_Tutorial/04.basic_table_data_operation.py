"""
표 데이터 연산
판다스의 Series 데이터 DataFrame 데이터의 연산을 살펴봅니다.
"""
import pandas as pd

s1 = pd.Series([10, 20, 30, 40, 50])
s2 = pd.Series([1, 2, 3, 4])

print("[ Series 데이터 연산 ]")
print("s1 = pd.Series([10, 20, 30, 40, 50])")
print("s2 = pd.Series([1, 2, 3, 4])")
# 사칙연산
print("- s1 + s2=\n{0}".format(s1 + s2))
print("- s1 - s2=\n{0}".format(s1 - s2))
print("- s1 * s2=\n{0}".format(s1 * s2))
print("- s1 / s2=\n{0}".format(s1 / s2))

# 기타 연산
print("- s1 + 5=\n{0}".format(s1 + 5))
print("- s1 ** 2=\n{0}".format(s1 ** 2))
print("- s1 > 30=\n{0}".format(s1 > 30))

print("[ DataFrame 데이터끼리의 연산 ]")
dict_data1 = {'A': [1,2,3,4,5],
              'B': [10, 20, 30, 40, 50],
              'C': [100, 200, 300, 400, 500]}
df1 = pd.DataFrame(dict_data1)
print("dict_data1 = {'A': [1,2,3,4,5],\n"
      "              'B': [10, 20, 30, 40, 50],\n"
      "              'C': [100, 200, 300, 400, 500]}\n")
print("pd.DataFrame(dict_data1) =\n", df1)

dict_data2 = {'A': [6,7,8,9],
              'B': [60, 70, 80, 90],
              'D': [600, 700, 800, 900]}
df2 = pd.DataFrame(dict_data2)
print("dict_data2 = {'A': [6,7,8,9],\n"
      "              'B': [60, 70, 80, 90],\n"
      "              'D': [600, 700, 800, 900]}\n")
print("pd.DataFrame(dict_data2) =\n", df2)

# DataFrame 데이터의 사칙 연산
print('DataFrame 데이터의 사칙 연산')
print("- df1 + df2=\n{0}".format(df1 + df2))
print("- df1 - df2=\n{0}".format(df1 - df2))
print("- df1 * df2=\n{0}".format(df1 * df2))
print("- df1 / df2=\n{0}".format(df1 / df2))

# DataFrame 데이터의 기타 연산
print('DataFrame 데이터의 기타 연산')
print("- df1 + 5=\n{0}".format(df1 + 5))
print("- df1 ** 2=\n{0}".format(df1 ** 2))
print("- df1 > 30=\n{0}".format(df1 > 30))
