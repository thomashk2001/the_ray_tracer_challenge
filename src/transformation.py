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

class ViewTransform(Matrix):
  def __init__(self, from_p, to, up):
    super().__init__(size = 4, default_value = 0)
    forward = to - from_p
    forward = forward.normalize()
    upn = up.normalize()
    left = forward.cross(upn)
    true_up = left.cross(forward)
    orientation = Matrix(size= 4, default_value= 0)
    orientation[0][0] = left.x
    orientation[0][1] = left.y
    orientation[0][2] = left.z
    orientation[1][0] = true_up.x
    orientation[1][1] = true_up.y
    orientation[1][2] = true_up.z
    orientation[2][0] = -forward.x
    orientation[2][1] = -forward.y
    orientation[2][2] = -forward.z
    orientation[3][3] = 1
    self.matrix = orientation * Translation(-from_p.x, -from_p.y, -from_p.z)
