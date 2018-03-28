from math import sqrt

class MatrixError(Exception):
	pass

class Matrix:

	def __init__(self, *rows):
		if len(rows) == 0:
			raise MatrixError("Cannot create empty Matrix.")
		size = len(rows)
		test_size_list = [len(row) for row in rows]
		for row_size in test_size_list:
			if row_size != size:
				raise MatrixError("Cannot create not square Matrix.")

		self._dim = len(rows)
		self._arr = list(rows)


	@staticmethod
	def construct(*args):
		size = len(args)
		if size == 0:
			raise MatrixError("Cannot create empty Matrix.")
		
		dim = int(sqrt(size))
		if not sqrt(size).is_integer():
			raise MatrixError("Cannot create not square matrix.")

		return Matrix(*[args [i * dim : (i + 1) * dim] for i in range(dim)])


	def __str__(self):
		s='\n'.join([' '.join([str(item) for item in row]) for row in self._arr])
		return s + '\n'
	
	def __getitem__(self, index):
		return self._arr[index]

	def __setitem__(self, index, value):
		self._arr[index] = value


	def __add__(self, to_add):
		if isinstance(to_add, int):
			matrix_to_add = [to_add] * self._dim**2
			return self + Matrix.construct(*matrix_to_add)

		if to_add._dim != self._dim:
			raise MatrixError("Cannot add matrixes of different sizes.")

		result = []
	
		for i in range(self._dim):
			for j in range(self._dim):
				result.append(self._arr[i][j] + to_add._arr[i][j])

		return Matrix.construct(*result)

	def __radd__(self, to_add):
		return self.__add__(to_add)

	def __sub__(self, to_sub):
		if isinstance(to_sub, int):
			matrix_to_sub = [to_sub] * self._dim**2
			return self - Matrix.construct(*matrix_to_sub)

		if to_sub._dim != self._dim:
			raise MatrixError("Cannot subtract matrixes of different sizes.")

		result = []
	
		for i in range(self._dim):
			for j in range(self._dim):
				result.append(self._arr[i][j] - to_sub._arr[i][j])

		return Matrix.construct(*result)

	def __rsub__(self, to_sub):
		if isinstance(to_sub, int):
			matrix_to_sub = [to_sub] * self._dim**2
			return Matrix.construct(*matrix_to_sub) - self

		if to_sub._dim != self._dim:
			raise MatrixError("Cannot subtract matrixes of different sizes.")

		result = []
	
		for i in range(self._dim):
			for j in range(self._dim):
				result.append(to_sub._arr[i][j] - self._arr[i][j])

		return Matrix.construct(*result)