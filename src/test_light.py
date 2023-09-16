from light import *
import unittest

class TestLight(unittest.TestCase):
  def test_light_with_position_intensity(self):
    intensity = Color(1, 1, 1)
    position = Point(0, 0, 0)
    light = Light(position, intensity)
    self.assertEqual(intensity, light.intensity)
    self.assertEqual(position, light.position)
    