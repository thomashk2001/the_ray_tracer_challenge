from tuple import *
from copy import copy

class Ray():
  def __init__(self, origin, direction):
    self.origin = copy(origin)
    self.direction = copy(direction)
    
  def position(self, t):
    return self.origin + self.direction * t
  