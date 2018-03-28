from matrix import Matrix

def run():

	rows = [[1, 2, 3], 
		[4, 5, 6],
		[7, 8, 9]]

	matrix1 = Matrix(*rows)


	matrix2 = Matrix(*[[9, 8, 7], 
		[6, 5, 4],
		[3, 2, 1]])

	matrix3 = Matrix.construct(1,2,3,4)
	print(matrix3)

	print("Matrix 1:")
	print(matrix1)

	print("Matrix 2:")
	print(matrix2)

	print("Matrix1 + Matrix2:")
	matrix_temp = matrix1 + matrix2
	print(matrix_temp)

	print("Matrix1 - Matrix2:")
	matrix_temp = matrix1 - matrix2
	print(matrix_temp)

	print("Matrix1 + 1:")
	matrix_temp = matrix1 + 1
	print(matrix_temp)
	
	print("2 + Matrix2:")
	matrix_temp = 2 + matrix2
	print(matrix_temp)

	print("Matrix1 - 1:")
	matrix_temp = matrix1 - 1
	print(matrix_temp)
	
	print("2 - Matrix2:")
	matrix_temp = 2 - matrix2
	print(matrix_temp)


if __name__ == "__main__":
	run()