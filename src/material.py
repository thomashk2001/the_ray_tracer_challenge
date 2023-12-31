from tuple import *

class Material():
  def __init__(self, color = Color(1, 1, 1), ambient = 0.1, diffuse = 0.9, 
               specular = 0.9, shininess = 200.0):
    self.color = color
    self.ambient = ambient
    self.diffuse = diffuse
    self.specular = specular
    self.shininess = shininess
    
  def __eq__(self, other):
    return self.color == other.color and self.ambient == other.ambient and \
      self.diffuse == other.diffuse and self.specular == other.specular and \
      self.shininess == other.shininess