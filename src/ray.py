from tuple import *
from copy import copy

class Ray():
  def __init__(self, origin, direction):
    self.origin = copy(origin)
    self.direction = copy(direction)
    
  def position(self, t):
    return self.origin + self.direction * t
  
  def transform(self, matrix):
    new_origin = matrix * self.origin
    print(new_origin)
    new_direction = matrix * self.direction
    print(new_direction)
    return Ray(new_origin, new_direction)