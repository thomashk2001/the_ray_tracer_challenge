import unittest
from intersections import *
from sphere import *
class TestSpheres(unittest.TestCase):
  def test_intersection_encapsulates_t_object(self):
    s = Sphere()
    i = Intersection(3.5, s)
    self.assertEqual(i.t, 3.5)
    self.assertEqual(i.object, s)
    
  def test_aggregating_intersections(self):
    s = Sphere()
    i1 = Intersection(1, s)
    i2 = Intersection(2, s)
    xs = Intersections(i1, i2)
    self.assertEqual(xs.count, 2)
    self.assertEqual(xs[0].object, s)
    self.assertEqual(xs[1].object, s)

  def test_hit_all_intersection_positive(self):
    s = Sphere()
    i1 = Intersection(1, s)
    i2 = Intersection(2, s)
    xs = Intersections(i1, i2)
    i = xs.hits()
    self.assertEqual(i, i1)
    
  def test_hit_some_intersection_negative(self):
    s = Sphere()
    i1 = Intersection(-1, s)
    i2 = Intersection(1, s)
    xs = Intersections(i1, i2)
    i = xs.hits()
    self.assertEqual(i, i2)
  
  def test_hit_all_intersection_negative(self):
    s = Sphere()
    i1 = Intersection(-5, s)
    i2 = Intersection(-7, s)
    xs = Intersections(i1, i2,)
    i = xs.hits()
    self.assertEqual(i, None)
  
  def test_hit_is_always_the_lowest_non_negative(self):
    s = Sphere()
    i1 = Intersection(5, s)
    i2 = Intersection(7, s)
    i3 = Intersection(-3, s)
    i4 = Intersection(2, s)
    xs = Intersections(i1, i2, i3, i4)
    i = xs.hits()
    self.assertEqual(i, i4)


