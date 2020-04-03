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

# test_matrix = np.arange(1,13).reshape(3,4)
# print(test_matrix.mean()) # mean = 평균
# print(test_matrix.std()) # std = 표준 편차

# vstack
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# print(np.vstack((a,b)))
# print('##############')
# # hstack
# a = np.array( [[1], [2], [3]] )
# b = np.array( [[4], [5], [6]] )
# print(np.hstack((a,b)))
# print('##############')
# a = np.array([[1, 2, 3]])
# b = np.array([[4, 5, 6]])
# print(np.concatenate((a,b), axis=0))
# print('##############')
# a = np.array([[1,2],[3,4]])
# b = np.array([[5,6]])
# print(np.concatenate((a,b.T), axis=1))
# test_array = np.array(["1", "4", 5, 8], np.float32)
# print(np.array(test_array).reshape(-1,2).shape )
# flatten_test = np.array([[["1", "4", 5, 8],["1", "4", 5, 8]],[["1", "4", 5, 8],["1", "4", 5, 8]]], int)
# print(flatten_test.flatten())



# test_array = np.array([1, 4, 0, 2, 3, 8, 9, 7], float)
# condition = test_array > 3
# print(condition) # 조건에 따른 true false 리턴함
# result = test_array[condition]
# print(result) # true 값인 인덱스의 실제값을 뽑아낼수 있다...
#
# condition.astype(np.int)
# print(condition.astype(np.int))
#
#
# a = np.array([2, 4, 6, 8], float)
# b = np.array([0, 0, 1, 3, 2, 1], int) # 반드시 integer로 선언해야함
# print(a[b]) # bracket index, b 배열의 값을 index로 하여 a의 값들을 추출함
#
# print(a.take(b))

a_int = np.array(
        [[  1900.,  30000.,   4000.,  48300.],
       [  1901.,  47200.,   6100.,  48200.],
       [  1902.,  70200.,   9800.,  41500.],
       [  1903.,  77400.,  35200.,  38200.],
       [  1904.,  36300.,  59400.,  40600.],
       [  1905.,  20600.,  41700.,  39800.],
       [  1906.,  18100.,  19000.,  38600.],
       [  1907.,  21400.,  13000.,  42300.],
       [  1908.,  22000.,   8300.,  44500.],
       [  1909.,  25400.,   9100.,  42100.]], int)
print(a_int.astype(int))
np.savetxt('int_data.csv',a_int,fmt="%2d", delimiter=",",header="문서제목")

np.save("npy_test", arr=a_int)
npy_array = np.load(file="npy_test.npy")
print(npy_array)
