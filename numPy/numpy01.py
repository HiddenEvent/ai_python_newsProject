import numpy as np

# test_array = np.array(["1", "4", 5, 8], np.float32)
# print(test_array)
# print(type(test_array[3]))

# test_array = np.array([["1", "4", 5, 8],["1", "4", 5, 8]], int)
# print(test_array[0][0])
# print(test_array[0,0])

# test_array = np.array([["1", "2", 3, 4, 5],["6", "7", 8, 9, 10]], int)
# print(test_array[:, 2:])  # 전체 Row의 2열 이상
# print(test_array[1, 1:3]) # 1 Row의 1열 ~ 2열
# print(test_array[1:3])   # 1 Row ~ 2 Row의 전체
# test_arr = np.arange(30).reshape(-1,5)
# print(test_arr)
# test_arr =np.zeros(shape=(10,), dtype=np.int8)
# print(test_arr)
#
# test_arr = np.ones(shape=(10,), dtype=np.int8)
# print(test_arr)
# test_matrix = np.arange(30).reshape(5,6)
# test_matrix = np.ones_like(test_matrix)
# print(test_matrix)
#
# test_matrix = np.arange(30).reshape(5,6)
# test_matrix = np.zeros_like(test_matrix)
# print(test_matrix)

# test_matrix = np.identity(n=3, dtype=np.int8)
# print(test_matrix)
#
# test_matrix = np.identity(6)
# print(test_matrix)

# test_matrix = np.eye(N=3, M=5, dtype=np.int8)
# print(test_matrix)
#
# test_matrix = np.eye(3, 5, k=2)
# print(test_matrix)
# test_matrix = np.arange(9).reshape(3,3)
# print(test_matrix)
# print(np.diag(test_matrix))

# test_matrix = np.arange(1,13).reshape(3,4)
# print(test_matrix)
# print(test_matrix.sum(axis=1)) # Column을 기준으로 더해라
# print(test_matrix.sum(axis=0)) # Row를 기준으로 더해라

test_matrix = np.arange(1,13).reshape(3,4)
print(test_matrix.mean()) # mean = 평균
print(test_matrix.std()) # std = 표준 편차


# test_array = np.array(["1", "4", 5, 8], np.float32)
# print(np.array(test_array).reshape(-1,2).shape )
# flatten_test = np.array([[["1", "4", 5, 8],["1", "4", 5, 8]],[["1", "4", 5, 8],["1", "4", 5, 8]]], int)
# print(flatten_test.flatten())