from matrix import Matrix
from matrix import identity_matrix
from math import sin
from math import cos
from math import pi
class Translation(Matrix):
  def __init__(self, x, y, z):
    super().__init__(size=4, default_value=0)
    self.matrix = identity_matrix().matrix
    self[0][3] = x
    self[1][3] = y
    self[2][3] = z

class Scaling(Matrix):
  def __init__(self, x, y, z):
    super().__init__(size= 4, default_value= 0)
    self.matrix = identity_matrix().matrix
    self[0][0] = x
    self[1][1] = y
    self[2][2] = z

class RotationX(Matrix):
  def __init__(self, radians):
    super().__init__(size = 4, default_value = 0)
    self.matrix = identity_matrix().matrix
    result_cos = cos(radians)
    result_sin = sin(radians)
    self[1][1] = result_cos
    self[1][2] = -result_sin
    self[2][1] = result_sin
    self[2][2] = result_cos

class RotationY(Matrix):
  def __init__(self, radians):
    super().__init__(size = 4, default_value = 0)
    self.matrix = identity_matrix().matrix
    result_cos = cos(radians)
    result_sin = sin(radians)
    self[0][0] = result_cos
    self[0][2] = result_sin
    self[2][0] = -result_sin
    self[2][2] = result_cos

class RotationZ(Matrix):
  def __init__(self,radians):
    super().__init__( size = 4, default_value = 0)
    self.matrix = identity_matrix().matrix
    result_cos = cos(radians)
    result_sin = sin(radians)
    self[0][0] = result_cos
    self[0][1] = -result_sin
    self[1][0] = result_sin
    self[1][1] = result_cos

class Shearing(Matrix):
  def __init__(self,  x_y = 0, x_z = 0, y_x = 0, y_z = 0, z_x = 0, z_y = 0):
    super().__init__(size = 4, default_value = 0)
    self.matrix = identity_matrix().matrix
    self[0][1] = x_y
    self[0][2] = x_z
    self[1][0] = y_x
    self[1][2] = y_z
    self[2][0] = z_x
    self[2][1] = z_y
