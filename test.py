# https://github.com/ptr97/kol1_gr1
import unittest
from matrix import Matrix, MatrixError

class TestMatrix(unittest.TestCase):
    def test_create_matrix(self):
        rows = [[1,2,3],
            [4,5,6],
            [7,8,9]]
        Matrix(*rows)
        
    def test_get_element(self):
        rows = [[1,2,3],[4,5,6],[7,8,9]]
        m = Matrix(*rows)
        self.assertEquals(m[0][0], 1)

    def test_construct_matrix(self):
        m = Matrix.construct(1,2,3,4)
        self.assertEquals(m, Matrix([1,2],[3,4]))

    def test_set_element(self):
        rows = [[1,2,3],
            [4,5,6],
            [7,8,9]]
        m = Matrix(*rows)
        m[0][1] = 12
        self.assertEquals(m[0][1], 12)

    def test_get_row(self):
        rows = [[1,2,3],
            [4,5,6],
            [7,8,9]]
        m = Matrix(*rows)
        self.assertEquals(m[0], [1,2,3])
    
    def test_set_row(self):
        rows = [[1,2,3],
            [4,5,6],
            [7,8,9]]
        m = Matrix(*rows)
        m[0] = [4,5,6]

    def test_add_matrix_of_ones(self):
        m = Matrix([1,2,3],[4,5,6],[7,8,9])
        self.assertEquals(1 + m, Matrix([2,3,4],[5,6,7],[8,9,10]))

    def test_add_matrix_to_matrix(self):
        m1 = Matrix([0,0,0],[0,0,0],[0,0,0])
        m2 = Matrix([1,1,1],[1,1,1],[1,1,1])
        self.assertEquals(m1+m2, Matrix([1,1,1],[1,1,1],[1,1,1]))

    def test_multiply_matrix_by_scalar(self):
        m = Matrix([1,1,1],[1,1,1],[1,1,1])
        self.assertEquals(2 * m, Matrix([2,2,2],[2,2,2],[2,2,2]))

    def test_multiply_matrixes(self):
        m = Matrix([1,2,3],[4,5,6],[7,8,9])
        self.assertEquals(m * m, Matrix([30,36,42],[66,81,96],[102,126,150]))

    def test_create_invalid_row_matrix(self):
        with self.assertRaises(MatrixError):
            Matrix([1,2,3],
                   [1,2],
                   [1,2,3])

    def test_empty_matrix(self):
    	with self.assertRaises(MatrixError):
            Matrix()

if __name__ == '__main__':
    unittest.main()