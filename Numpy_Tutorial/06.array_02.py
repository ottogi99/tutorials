# 배열 데이터의 집계 및 통계 연산

import numpy as np

arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([1, 2, 3, 4])

print('덧셈:', arr1 + arr2)  # 덧셈
print('뺄셈:', arr1 - arr2)  # 뺄셈
print('곱셈:', arr1 * arr2)  # 곱셈
print('나눗셈:', arr1 / arr2)  # 나눗셈

print('배열의 각 요소에 상수 덧셈:', arr2 + 10)
print('배열의 각 요소에 상수 뺄셈:', arr2 - 1)
print('배열의 각 요소에 상수 곱셈:', arr2 * 2)
print('배열의 각 요소에 상수 나눗셈:', arr2 / 10)
print('배열의 각 요소에 거듭제곱:', arr2 ** 2)
print('배열의 각 요소에 비교연산:', arr1 >= 30)


# -- 배열 데이터의 집계 및 통계 연산
# 배열의 합: sum()
# 배열의 평균: mean()
# 배열의 표준편차: std() (standard devation)
# 배열의 분산: var() (variation)
# 배열의 최소값: min()
# 배열의 최대값: max()
# 배열의 누적합: cumsum() (cumulative sum)
# 배열의 누적곱: cumprod() (cumulative product)

print('\n - 배열의 합, 평균')
arr3 = np.array([1, 2, 3, 4, 5])
print('[1, 2, 3, 4, 5]의 합: {0}, 평균: {1}'.format(arr3.sum(), arr3.mean()))
print('[1, 2, 3, 4, 5]의 표준편차: {0}, 분산: {1}'.format(arr3.std(), arr3.var()))
print('[1, 2, 3, 4, 5]의 최소: {0}, 최대: {1}'.format(arr3.min(), arr3.max()))
print('[1, 2, 3, 4, 5]의 누적합: {0}, 누적곱: {1}'.format(arr3.cumsum(), arr3.cumprod()))

# -- 배열의 데이터 선택
print('\n - 1차원 배열에서 여러 개의 요소를 가져오려면 각 요소의 위치를 리스트로 지정')
a2 = np.array([0, 10, 20, 30, 40, 50])
print('a2=[0, 10, 20, 30, 40, 50]\na2[[4, 0, 5, -1, -2]] = {0}'.format(a2[[4, 0, 5, -1, -2]]))

print('\n - 배열에 조건 지정')
a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
a = np.arange(0, 9, 1)
print('a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\na[a >= 5] = {0}'.format(a[a >= 5]))

print('\n - 조건 (짝수)')
print('a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\na[(a % 2) == 0] = {0}'.format(a[(a % 2) == 0]))

print('\n - 조건 (논리식)')
print('a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\na[((a % 2) == 0) & (a > 5)] = {0}'.format(a[((a % 2) == 0) & (a > 5)]))

print('\n - 배열 슬라이싱 (배열[start:end:step])')
a2 = np.arange(0, 100, 10)
print('a=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]\na2[0:10:2] = {0}'.format(a2[0:10:2]))

print('\n - 배열 슬라이싱 역순(배열[start:end:step(음수)])')
print('a=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]\na2[::-1] = {0}'.format(a2[::-1]))
print('a=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]\na2[8:2:-2] = {0}'.format(a2[8:2:-2]))

