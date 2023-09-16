from material import *
from light import *
from light import lighting
import unittest

class TestMaterial(unittest.TestCase):
  def background(self):
    return(Material(), Point(0, 0, 0))
  def test_default_material(self):
    m = Material()
    self.assertEqual(m.color, Color(1, 1, 1))
    self.assertEqual(m.ambient, 0.1)
    self.assertEqual(m.diffuse, 0.9)
    self.assertEqual(m.specular, 0.9)
    self.assertEqual(m.shininess, 200.0)
  
  def test_lighting_with_eye_between_light_and_surface(self):
    m , position = self.background()
    eyev = Vector(0, 0, -1)
    normalv = Vector(0, 0, -1)
    light = Light(Point(0, 0, -10), Color(1, 1, 1))
    result = lighting(m, light, position, eyev, normalv)
    print(type(result))
    self.assertEqual(True, isinstance(result, Color))
    self.assertEqual(result, Color(1.9, 1.9, 1.9))
  
  def test_lighting_with_eye_between_light_and_surface_offset_45(self):
    m , position = self.background()
    eyev = Vector(0, sqrt(2)/2, -sqrt(2)/2)
    normalv = Vector(0, 0, -1)
    light = Light(Point(0, 0, -10), Color(1, 1, 1))
    result = lighting(m, light, position, eyev, normalv)
    self.assertEqual(True, isinstance(result, Color))
    self.assertEqual(result, Color(1, 1, 1))
  
  def test_lighting_with_eye_oposite_surface_light_offset_45(self):
    m, position = self.background()
    eyev = Vector(0, 0, -1)
    normalv = Vector(0, 0, -1)
    light = Light(Point(0, 10, -10), Color(1, 1, 1))
    result = lighting(m, light, position, eyev, normalv)
    self.assertEqual(True, isinstance(result, Color))
    self.assertEqual(result, Color(0.7364, 0.7364, 0.7364))
  
  def test_lighting_with_eye_in_path_of_reflect_vector(self):
    m, position = self.background()
    eyev = Vector(0, -sqrt(2)/2, -sqrt(2)/2)
    normalv = Vector(0, 0, -1)
    light = Light(Point(0, 10, -10), Color(1, 1, 1))
    result = lighting(m, light, position, eyev, normalv)
    self.assertEqual(True, isinstance(result, Color))
    self.assertEqual(result, Color(1.6364, 1.6364, 1.6364))
  
  def test_lighting_with_light_behind_surface(self):
    m, position = self.background()
    eyev = Vector(0, 0, -1)
    normalv = Vector(0, 0, -1)
    light = Light(Point(0, 0, 10), Color(1, 1, 1))
    result = lighting(m, light, position, eyev, normalv)
    self.assertEqual(True, isinstance(result, Color))
    self.assertEqual(result, Color(0.1, 0.1, 0.1))
