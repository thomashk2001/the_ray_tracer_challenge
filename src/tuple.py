import numpy as np
from constants import EPSILON
from math import sqrt

class Tuple:
  def __init__(self, x, y, z, w):
    self.x = x
    self.y = y
    self.z = z
    self.w = w

  def __str__(self):
      return f"[{self.x},{self.y},{self.z},{self.w}]"
    
  def __eq__(self, other):
    return abs(self.x - other.x) < EPSILON and abs(self.y - other.y) < EPSILON \
      and abs(self.z - other.z) < EPSILON and self.w == other.w
    
  def add(self, other):
    return(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)
  
  # add method has additional ifs to maintain class type accordingly in case 
  # of V + V, P + V or V + P. P:Point, V:Vector
  def __add__(self, other):
    if self.w and other.w: # TODO:change to assert to disable on main run
      raise("Error: Adding points not allowed")
    x,y,z,w = self.add(other)
    if self.w:  #TODO: DECIDE THIS !
      return Point(x,y,z,w)
    else:
      return Vector(x,y,z,w)
    
  def sub(self, other):
    return(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)
  
  def __sub__(self, other):
    if self.w - other.w == -1:
      raise("Error: Subtraction of vector - point not allowed")
    x,y,z,w = self.sub(other)
    if w:
      return Point(x,y,z)
    else:
      return Vector(x,y,z)
  
  def __neg__(self):
    if isinstance(self, Point):
      raise("Error: Negating points not allowed")
    return self.__class__(-self.x, -self.y, -self.z, -self.w)
  
  def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float) and not isinstance(self, Point):
            return self.__class__(self.x * other, self.y * other, self.z * other, self.w * other)
        else:
           raise ("Error: Only multiplication of scalar and vectors allowed!")
  
  def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float) and not isinstance(self, Point):
            return self.__class__(self.x / other, self.y / other, self.z / other, self.w / other)
        else:
           raise ("Error: Only division of scalar and vectors allowed!")
class Point(Tuple):
  def __init__(self, x, y, z, w=1):
    super().__init__(x, y, z, w)

class Vector(Tuple):
  def __init__(self, x, y, z, w=0):
    super().__init__(x, y, z, w) 
  
  def magnitud(self):
    return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2 + self.w ** 2)
  
  def normalize(self):
    magnitude = self.magnitud()
    return Vector(self.x/magnitude, self.y/magnitude, self.z/magnitude)
  
  def dot(self, other):
    return self.x * other.x + self.y * other.y + self.z * other.z
  
  def cross(self, other):
    return Vector(self.y * other.z - self.z * other.y,
                  self.z * other.x - self.x * other.z,
                  self.x * other.y - self.y * other.x)
