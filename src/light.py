from tuple import *
from copy import copy
from material import *
class Light():
  def __init__(self, position , intensity):
    self.intensity = copy(intensity)
    self.position = copy(position)
  
  def __eq__(self, other):
    return self.intensity == other.intensity and self.position == other.position

def lighting(material, light, point, eyev, normalv):
  effective_color = material.color * light.intensity
  lightv = light.position - point
  lightv = lightv.normalize()
  ambient = effective_color * material.ambient
  light_dot_normal = lightv.dot(normalv)
  if light_dot_normal < 0:
    diffuse = Color(0, 0, 0)
    specular = Color(0, 0, 0)
  else:
    diffuse = effective_color * material.diffuse * light_dot_normal
    reflectv = -lightv.reflect(normalv)
    reflect_dot_eye = reflectv.dot(eyev)
    if reflect_dot_eye <= 0:
      specular = Color(0, 0, 0)
    else:
      factor = pow(reflect_dot_eye, material.shininess)
      specular = light.intensity * material.specular * factor
  return ambient + diffuse + specular