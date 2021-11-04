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



