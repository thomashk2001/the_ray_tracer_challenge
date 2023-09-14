import unittest
from tuple import *
from ray import *

class TestRays(unittest.TestCase):
  def test_create_ray(self):
    origin = Point(1, 2, 3)
    direction = Vector(4, 5, 6)
    r = Ray(origin, direction)
    self.assertEqual(r.origin, origin)
    self.assertEqual(r.direction, direction)
  
  def test_computing_point_from_distance(self):
    r = Ray(Point(2, 3, 4), Vector(1, 0, 0))
    self.assertEqual(r.position(0), Point(2, 3, 4))
    self.assertEqual(r.position(1), Point(3, 3, 4))
    self.assertEqual(r.position(-1), Point(1, 3, 4))
    self.assertEqual(r.position(2.5), Point(4.5, 3, 4))
    
