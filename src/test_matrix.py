import unittest
from matrix import *
class TestMatrix(unittest.TestCase):
  def test_construct_inspect_4by4_matrix(self):
    M = Matrix()
    print()
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