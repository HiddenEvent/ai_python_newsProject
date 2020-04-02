from functools import reduce

# TODO Problem #1 - vector_size_check (one line code available)
def vector_size_check(*vector_variables):
#   내가 푼 것
#   코드를 더 줄일 수 있구나...
    result = all([len(vector_variables[0]) == vector_len for vector_len in [len(vector) for vector in vector_variables]])
#   해설
#   test = all(len(vector_variables[0]) == x for x in [len(vector) for vector in vector_variables[1:]])
    return result
# print(vector_size_check([1,2,3], [2,3,4], [5,6,7])) # Expected value: True
# print(vector_size_check([1, 3], [2,4], [6,7])) # Expected value: True
# print(vector_size_check([1, 3, 4], [4], [6,7])) # Expected value: False

# TODO Problem #2 - vector_addition (one line code available)
def vector_addition(*vector_variables):
    result = [sum(vactor) for vactor in zip(*vector_variables)]
    return result

# 실행결과
# print(vector_addition([1, 3], [2, 4], [6, 7])) # Expected value: [9, 14]
# print(vector_addition([1, 5], [10, 4], [4, 7])) # Expected value: [15, 16]
# print(vector_addition([1, 3, 4], [4], [6,7])) # Expected value: ArithmeticError

# TODO Problem #3 - vector_subtraction (one line code available)
def vector_subtraction(*vector_variables):
    if vector_size_check(*vector_variables) == False:
        raise ArithmeticError
#   내가 푼 것
#     result = [reduce(lambda x, y: x - y, vector) for vector in zip(*vector_variables)]
#   해설
    result = [vector[0] * 2 - sum(vector) for vector in zip(*vector_variables)]
    return result
# 실행결과
# print(vector_subtraction([1, 3], [2, 4])) # Expected value: [-1, -1]
# print(vector_subtraction([1, 5], [10, 4], [4, 7])) # Expected value: [-13, -6]

# TODO Problem #4 - scalar_vector_product (one line code available)
def scalar_vector_product(alpha, vector_variable):
    result = [alpha * vector for vector in vector_variable]
    return result
# 실행결과
# print (scalar_vector_product(5,[1,2,3])) # Expected value: [5, 10, 15]
# print (scalar_vector_product(3,[2,2])) # Expected value: [6, 6]
# print (scalar_vector_product(4,[1])) # Expected value: [4]

# TODO Problem #5 - matrix_size_check (one line code available)
def matrix_size_check(*matrix_variables):
    # 내가 푼거... col 갯수에 대해서만 구한거였다... row 갯수도 같은지 확인해야 한다..
    # result = all([len(matrix_variables[0]) == len(matrix_variable) for matrix_variable in matrix_variables])
    result = all([len(set(len(matrix[0]) for matrix in matrix_variables)) == 1]) and all([len(matrix_variables[0]) == len(matrix) for matrix in matrix_variables])
    return result
# 실행결과
# matrix_x = [[2, 2], [2, 2], [2, 2]]
# matrix_y = [[2, 5], [2, 1]]
# matrix_z = [[2, 4], [5, 3]]
# matrix_w = [[2, 5], [1, 1], [2, 2]]
#
# print (matrix_size_check(matrix_x, matrix_y, matrix_z)) # Expected value: False
# print (matrix_size_check(matrix_y, matrix_z)) # Expected value: True
# print (matrix_size_check(matrix_x, matrix_w)) # Expected value: True

# TODO Problem #6 - is_matrix_equal (one line code available)
def is_matrix_equal(*matrix_variables):
    result = all([ all([len(set(row)) == 1 for  row in zip(*matrix)]) for matrix in zip(*matrix_variables)])
    return result
# matrix_x = [[2, 2], [2, 2]]
# matrix_y = [[2, 5], [2, 1]]
#
# print (is_matrix_equal(matrix_x, matrix_y, matrix_y, matrix_y)) # Expected value: False
# print (is_matrix_equal(matrix_x, matrix_x)) # Expected value: True

# TODO Problem #7 - matrix_addition (one line code available)
def matrix_addition(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    result = [[sum(element) for element in zip(*matrix)] for matrix in zip(*matrix_variables)]
    return result
# 실행결과
# matrix_x = [[2, 2], [2, 2]]
# matrix_y = [[2, 5], [2, 1]]
# matrix_z = [[2, 4], [5, 3]]
#
# print (matrix_addition(matrix_x, matrix_y)) # Expected value: [[4, 7], [4, 3]]
# print (matrix_addition(matrix_x, matrix_y, matrix_z)) # Expected value: [[6, 11], [9, 6]]

# TODO Problem #8 - matrix_subtraction (one line code available)
def matrix_subtraction(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    result = [[element[0]*2 - sum(element) for element in zip(*matrix)] for matrix in zip(*matrix_variables)]
    return result

# 실행결과
# matrix_x = [[2, 2], [2, 2]]
# matrix_y = [[2, 5], [2, 1]]
# matrix_z = [[2, 4], [5, 3]]
#
# print (matrix_subtraction(matrix_x, matrix_y)) # Expected value: [[0, -3], [0, 1]]
# print (matrix_subtraction(matrix_x, matrix_y, matrix_z)) # Expected value: [[-2, -7], [-5, -2]]

# TODO Problem #9 - matrix_transpose (one line code available)
def matrix_transpose(matrix_variable):
    result = [[i for i in matrix] for matrix in zip(*matrix_variable)]
    print(result)
    return result

# 실행결과
# matrix_w = [[2, 5], [1, 1], [2, 2]]
# matrix_transpose(matrix_w)

# TODO Problem #10 - scalar_matrix_product (one line code available)
def scalar_matrix_product(alpha, matrix_variable):
    result = [scalar_vector_product(alpha, matrix) for matrix in matrix_variable]
    return result

# 실행결과
# matrix_x = [[2, 2], [2, 2], [2, 2]]
# matrix_y = [[2, 5], [2, 1]]
# matrix_z = [[2, 4], [5, 3]]
# matrix_w = [[2, 5], [1, 1], [2, 2]]
#
# print(scalar_matrix_product(3, matrix_x)) #Expected value: [[6, 6], [6, 6], [6, 6]]
# print(scalar_matrix_product(2, matrix_y)) #Expected value: [[4, 10], [4, 2]]
# print(scalar_matrix_product(4, matrix_z)) #Expected value: [[8, 16], [20, 12]]
# print(scalar_matrix_product(3, matrix_w)) #Expected value: [[6, 15], [3, 3], [6, 6]]

# TODO Problem #11 - is_product_availability_matrix (one line code available)
def is_product_availability_matrix(matrix_a, matrix_b):
    type1 = len([column_vector for column_vector in zip(*matrix_a)])
    type2 = len(matrix_b)
    result = type1 == type2
    return result
# 실행결과
# matrix_x= [[2, 5], [1, 1]]
# matrix_y = [[1, 1, 2], [2, 1, 1]]
# matrix_z = [[2, 4], [5, 3], [1, 3]]
#
# print(is_product_availability_matrix(matrix_y, matrix_z)) # Expected value: True
# print(is_product_availability_matrix(matrix_z, matrix_x)) # Expected value: True
# # print(is_product_availability_matrix(matrix_z, matrix_w)) # Expected value: False //matrix_w가없습니다
# print(is_product_availability_matrix(matrix_x, matrix_x)) # Expected value: True

# TODO Problem #12 - matrix_product (one line code available)
def matrix_product(matrix_a, matrix_b):
    if is_product_availability_matrix(matrix_a, matrix_b) == False:
        raise ArithmeticError
    result = [[sum(a*b for a, b in zip(column_b, row_a))for column_b in zip(*matrix_b)]for row_a in matrix_a]
    return result

# 실행결과
# matrix_x = [[2, 5], [1, 1]]
# matrix_y = [[1, 1, 2], [2, 1, 1]]
# matrix_z = [[2, 4], [5, 3], [1, 3]]
#
# print(matrix_product(matrix_y, matrix_z)) # Expected value: [[9, 13], [10, 14]]
# print(matrix_product(matrix_z, matrix_x)) # Expected value: [[8, 14], [13, 28], [5, 8]]
# print(matrix_product(matrix_x, matrix_x)) # Expected value: [[9, 15], [3, 6]]
# print(matrix_product(matrix_z, matrix_w)) # Expected value: False

