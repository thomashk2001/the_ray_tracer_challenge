import unittest
from matrix import *
class TestMatrix(unittest.TestCase):
  def test_construct_inspect_4by4_matrix(self):
    M = Matrix()
    M.matrix = [
      [1, 2, 3, 4],
      [5.5, 6.5, 7.5, 8.5],
      [9, 10, 11, 12],
      [13.5, 14.5, 15.5, 16.5]
      ]
    self.assertEqual(M[0][0], 1)
    self.assertEqual(M[0][3], 4)
    self.assertEqual(M[1][0], 5.5)
    self.assertEqual(M[1][2], 7.5)
    self.assertEqual(M[2][2], 11)
    self.assertEqual(M[3][0], 13.5)
    self.assertEqual(M[3][2], 15.5)
  
  def test_2by2_matrix(self):
    M = Matrix(2)
    M.matrix = [
       [-3, 5],[1, -2]
    ]
    self.assertEqual(M.size, 2)
    self.assertEqual(M[0][0], -3)
    self.assertEqual(M[0][1], 5)
    self.assertEqual(M[1][0], 1)
    self.assertEqual(M[1][1], -2)
  
  def test_3by3_matrix(self):
    M = Matrix(3)
    M.matrix = [
       [-3, 5, 0],
       [1, -2, -7],
       [0, 1, 1]
    ]
    self.assertEqual(M.size, 3)
    self.assertEqual(M[0][0], -3)
    self.assertEqual(M[0][1], 5)
    self.assertEqual(M[1][0], 1)
    self.assertEqual(M[1][1], -2)
    self.assertEqual(M[2][2], 1)
    
  def test_equality_identical_matrix(self):
    A = Matrix()
    B = Matrix()
    A.matrix = [
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 8, 7, 6],
      [5, 4, 3, 2]
    ]
    B.matrix = [
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 8, 7, 6],
      [5, 4, 3, 2]
    ]
    self.assertEqual(A, B)
  def test_equality_diff_matrix(self):
    A = Matrix()
    B = Matrix()
    A.matrix = [
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 8, 7, 6],
      [5, 4, 3, 2]
    ]
    B.matrix = [
      [1, 2, 3, 4],
      [5, 6, 5, 8],
      [9, 8, 7, 6],
      [5, 4, 3, 2]
    ]
    self.assertNotEqual(A, B)
    
  def test_multiplication_of_two_matrix(self):
    A = Matrix()
    B = Matrix()
    A.matrix = [
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 8, 7, 6],
      [5, 4, 3, 2]
    ]
    B.matrix = [
      [-2, 1, 2, 3],
      [3, 2, 1, -1],
      [4, 3, 6, 5],
      [1, 2, 7, 8]
    ]
    result = A * B
    expected = Matrix()
    expected.matrix = [
      [20, 22, 50, 48],
      [44, 54, 114, 108],
      [40, 58, 110, 102],
      [16, 26, 46, 42]
    ]
    self.assertEqual(result, expected)
    
  def test_multiplication_of_tuple_matrix(self):
    A = Matrix()
    A.matrix = [
      [1,2,3,4],
      [2,4,4,2],
      [8,6,4,1],
      [0,0,0,1]
    ]
    b = Tuple(1,2,3,1)
    result = A*b
    self.assertEqual(result, Tuple(18,24,33,1))
  
  def test_multiply_by_identity_matrix(self):
    A = Matrix()
    A.matrix = [
      [0,1,2,4],
      [1,2,4,8],
      [2,4,8,16],
      [4,8,16,32]
    ]
    self.assertEqual(A, A*identity_matrix())
    
  def test_transpose_matrix(self):
    A = Matrix()
    A.matrix = [
      [0, 9, 3, 0],
      [9, 8, 0, 8],
      [1, 8, 5, 3],
      [0, 0, 5, 8]
    ]
    A_transpose = Matrix()
    A_transpose.matrix = [
      [0, 9, 1, 0],
      [9, 8, 8, 0],
      [3, 0, 5, 5],
      [0, 8, 3, 8]
    ]
    self.assertEqual(A_transpose, A.transpose())
  
  def test_determinant_2by2_matrix(self):
    A = Matrix(2)
    A.matrix = [
      [1, 5],
      [-3, 2]
    ]
    self.assertEqual(A.determinant(), 17)
    
  def test_sub_matrix_3by3_matrix(self):
    A = Matrix(3)
    A.matrix = [
      [1, 5, 0],
      [-3, 2, 7],
      [0, 6, -3]
    ]
    expected = Matrix(2)
    expected.matrix = [
      [-3, 2], [0, 6]
    ]
    self.assertEqual(A.sub_matrix(0,2), expected)
    
  def test_sub_matrix_4by4_matrix(self):
    A = Matrix()
    A.matrix = [
      [-6, 1, 1, 6],
      [-8, 5, 8, 6],
      [-1, 0, 8, 2],
      [-7, 1, -1, 1]
    ]
    expected = Matrix(3)
    expected.matrix = [
      [-6, 1, 6],
      [-8, 8, 6],
      [-7, -1, 1]
    ]
    self.assertEqual(A.sub_matrix(2,1), expected)
  
  def test_minor_3by3_matrix(self):
    A = Matrix(3)
    A.matrix = [
      [3, 5, 0],
      [2, -1, -7],
      [6, -1, 5]
    ]
    B = A.sub_matrix(1, 0)
    self.assertEqual(B.determinant(), 25)
    self.assertEqual(A.minor(1, 0), 25)
    
  def test_cofactor_3by3_matrix(self):
    A = Matrix(3)
    A.matrix = [
      [3, 5, 0],
      [2, -1, -7],
      [6, -1, 5]
    ]
    self.assertEqual(A.minor(0,0), -12)
    self.assertEqual(A.cofactor(0,0), -12)
    self.assertEqual(A.minor(1,0), 25)
    self.assertEqual(A.cofactor(1,0), -25)
  
  def test_determinant_3by3_matrx(self):
    A = Matrix(3)
    A.matrix = [
      [1, 2, 6],
      [-5, 8, -4],
      [2, 6, 4]
    ]
    self.assertEqual(A.cofactor(0, 0), 56)
    self.assertEqual(A.cofactor(0, 1), 12)
    self.assertEqual(A.cofactor(0, 2), -46)
    self.assertEqual(A.determinant(), -196)
    
  def test_determinant_4by4_matrix(self):
    A = Matrix()
    A.matrix = [
      [-2, -8, 3, 5],
      [-3, 1, 7, 3],
      [1, 2, -9, 6],
      [-6, 7, 7, -9]
    ]
    self.assertEqual(A.cofactor(0, 0), 690)
    self.assertEqual(A.cofactor(0, 1), 447)
    self.assertEqual(A.cofactor(0, 2), 210)
    self.assertEqual(A.cofactor(0, 3), 51)
    self.assertEqual(A.determinant(), -4071)
  
  def test_is_invertible_matrix(self):
    A = Matrix()
    A.matrix = [
      [6, 4, 4, 4],
      [5, 5, 7, 6],
      [4, -9, 3, -7],
      [9, 1, 7, -6]
    ]
    self.assertEqual(A.determinant(), -2120)
    self.assertEqual(A.is_invertible(), True)
    
  def test_is_not_invertible(self):
    A = Matrix()
    A.matrix = [
      [-4, 2, -2, -3],
      [9, 6, 2, 6],
      [0, -5, 1, -5],
      [0,0,0,0]
    ]
    self.assertEqual(A.determinant(), 0)
    self.assertEqual(A.is_invertible(), False)
    
  def test_inverse_matrix(self):
    A = Matrix()
    A.matrix = [
      [-5, 2, 6, -8],
      [1, -5, 1, 8],
      [7, 7, -6, -7],
      [1, -3, 7, 4]]
    B = A.inverse()
    self.assertEqual(A.determinant(), 532)
    self.assertEqual(A.cofactor(2, 3), -160)
    self.assertEqual(B[3][2], -160/532)
    self.assertEqual(A.cofactor(3, 2), 105)
    self.assertEqual(B[2][3], 105/532)
    expected_matrix = Matrix()
    expected_matrix.matrix = [
      [0.21805, 0.45113, 0.24060, -0.04511],
      [-0.80827, -1.45677, -0.44361, 0.52068],
      [-0.07895, -0.22368, -0.05263, 0.19737],
      [0.52256, -0.81391, -0.30075, 0.30639]
    ]
    
  def test_inverse_2_matrix(self):
    A = Matrix()
    A.matrix = [
      [8, -5, 9, 2],
      [7, 5, 6, 1],
      [-6, 0, 9, 6],
      [-3, 0, -9, -4]
    ]
    expected_matrix = Matrix()
    expected_matrix.matrix = [
    [-0.15385, -0.15385, -0.28205 , -0.53846 ],
    [-0.07692, 0.12308, 0.02564, 0.03077 ],
    [0.35897, 0.35897, 0.43590, 0.92308 ],
    [-0.69231,-0.69231, -0.76923, -1.92308 ]
    ]
    self.assertEqual(A.inverse(), expected_matrix)
  
  def test_inverse_3_matrix(self):
    A = Matrix()
    A.matrix = [
      [9, 3, 0, 9],
      [-5, -2, -6, -3],
      [-4, 9, 6, 4],
      [-7, 6, 6, 2]
    ]
    expected_matrix = Matrix()
    expected_matrix.matrix = [
      [ -0.04074, -0.07778, 0.14444, -0.22222],
      [ -0.07778, 0.03333, 0.36667, -0.33333],
      [-0.02901, -0.14630, -0.10926, 0.12963],
      [0.17778, 0.06667, -0.26667, 0.33333],
    ]
    self.assertEqual(A.inverse(), expected_matrix)
    
  def test_multiply_product_by_inverse_matrix(self):
    A = Matrix()
    A.matrix = [
      [3, -9, 7, 3],
      [3, -8, 2, -9],
      [-4, 4, 4, 1],
      [-6, 5, -1, 1]
    ]
    B = Matrix()
    B.matrix = [
      [8, 2, 2, 2],
      [3, -1, 7, 0],
      [7, 0, 5, 4],
      [6, -2, 0, 5]
    ]
    C = A*B
    self.assertEqual(C* B.inverse(), A)