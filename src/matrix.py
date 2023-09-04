from tuple import *

class Matrix:
  def __init__(self, size = 4, default_value = None):
    if default_value is None:
      default_value = 0
    self.size = size
    self.matrix = [[default_value] * size for _ in range(size)]
  def __str__(self):
    string = ""
    for row in self.matrix:
      string+="|"
      for col in row:
        string+= str(col) +"|"
      string+="\n"
    return string
  
  def __getitem__(self, key):
    return self.matrix[key]
  
  def __eq__(self, other):
    if self.size != other.size:
      return False
    limit = self.size
    for row in range(limit):
      for col in range(limit):
        if self[row][col]!= other[row][col]:
          return False
    return True
  
  def __ne__(self, other):
    return not self == other
  
  def matrix_tuple_multiplication(self, tuple):
    result = []
    for row in self.matrix:
      result.append(row[0] * tuple.x + row[1] * tuple.y + row[2] * tuple.z + 
                    row[3] * tuple.w)
    return Tuple(result[0], result[1], result[2], result[3])
  
  def matrix_multiplication(self, other):
    limit = self.size
    result = Matrix(limit)
    for row in range(limit):
      for col in range(limit):
        for k in range(limit):
          result[row][col] += self[row][k] * other[k][col]
    return result

  def __mul__(self, other):
    if isinstance(other, Tuple):
      return self.matrix_tuple_multiplication(other)
    else:
      return self.matrix_multiplication(other)
    
  def transpose(self):
    limit = self.size
    result = Matrix(limit)
    for row in range(limit):
      for col in range(limit):
        result[col][row] = self[row][col]
    return result
  
  def determinant(self):
    determinant = 0
    if self.size == 2:
      determinant =  self[0][0]* self[1][1] - self[0][1] * self[1][0]
    else:
      determinant = 0
      limit = self.size
      for col in range(limit):
        determinant+= self[0][col] * self.cofactor(0, col)
    return determinant
  
  def sub_matrix(self, row, col):
    result = Matrix(self.size -1)
    temp = []
    limit = self.size
    for i in range(limit):
      if i == row:
        continue
      for j in range(limit):
        if j == col:
          continue
        temp.append(self[i][j])
    list_size = len(temp)
    result_size = result.size
    result.matrix = [temp[i:i+result_size]for i in range(0, list_size, result_size)]
    return result
  
  def minor(self, row, col):
    return self.sub_matrix(row, col).determinant()
  
  def cofactor(self, row, col):
    result = self.minor(row, col)
    if row + col % 2 != 0:
      result*= -1
    return result
def identity_matrix(size = 4):
  result = Matrix(size)
  for i in range(size):
    result[i][i] = 1
  return result