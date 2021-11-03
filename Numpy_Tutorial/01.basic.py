# 배열 데이터 연산에 효율적인 넘파이(NumPy)

import numpy as np

# 리스트 데이터로부터 배열을 생성
list_data = [0, 1, 2, 3, 4, 5.0]
a1 = np.array(list_data)
print(a1)

# 다차원 배열 생성
a2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a2)

# 수학에서는 1차원 배열은 벡터라고 하고 2차원 배열은 행렬이라고 합니다.

# 범위와 간격을 지정해 배열을 생성 ([start], stop[, step])
arr = np.arange(0, 10, 1)
print(arr)

# 범위와 개수를 지정해 배열을 생성 (start, stop[, num]), 간격은 (stop-start) / (num-1)
arr = np.linspace(0, np.pi, 20)
print(arr)


