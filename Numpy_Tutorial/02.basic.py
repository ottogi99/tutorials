# 배열 데이터 연산에 효율적인 넘파이(NumPy)

import numpy as np

# 배열 형태를 재구성
arr1 = np.array([0, 1, 2, 3, 4, 5])
arr2 = np.array([[0, 1, 2], [3, 4, 5]])

# 1차원 배열을 2차원 배열로 재구성
re_arr1 = arr1.reshape(2, 3)
# print(re_arr1)

# 2차원 배열을 1차원 배열로 재구성
re_arr2 = arr2.reshape(6,)
# print(re_arr2)

# 6x1 형태의 2차원 배열로 재구성
new_arr1 = arr1.reshape(6, 1)
print(new_arr1)

# 1x6 형태의 2차원 배열로 재구성
new_arr2 = arr1.reshape(1, 6)
print(new_arr2)

# 배열의 차원을 알아보는 arr.ndim
print([arr1.ndim, new_arr1.ndim])

# m이나 n 중 하나에만 값을 입력하고 나머지에 -1을 대입하면 넘파이 배열의 개수에 따라 자동으로 해당 자리의 값을 계산해 대입
# arr1.reshape(2, 3)과 동일
arr1.reshape(2, -1)

# arr1.reshape(3, 2)와 동일
arr1.reshape(-1, 2)

# arr.reshape(6, 1)과 동일, 2차원 배열 (m x n) (행, 열)
arr1.reshape(-1, 1)

# arr1.reshape(2, 3, 4), 3차원 배열 (l x m x n) (면, 행, 열)
arr_3d = np.arange(0, 24, 1).reshape(2, 3, -1)
print(arr_3d)


