import unittest
from tuple import *
from ray import *
from transformation import *

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
  
  def test_translating_a_ray(self):
    r = Ray(Point(1, 2, 3), Vector(0, 1, 0))
    m = Translation(3, 4, 5)
    r2 = r.transform(m)
    self.assertEqual(r2.origin, Point(4, 6, 8))
    self.assertEqual(r2.direction, Vector(0, 1, 0))
  
  def test_scaling_a_ray(self):
    r = Ray(Point(1, 2, 3), Vector(0, 1, 0))
    m = Scaling(2, 3, 4)
    r2 = r.transform(m)
    self.assertEqual(r2.origin, Point(2, 6, 12))
    self.assertEqual(r2.direction, Vector(0, 3, 0))
  
