import unittest
from intersections import *
from sphere import *
from ray import *
from transformation import *
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
    xs = Intersections([i1, i2])
    self.assertEqual(xs.count, 2)
    self.assertEqual(xs[0].object, s)
    self.assertEqual(xs[1].object, s)

  def test_hit_all_intersection_positive(self):
    s = Sphere()
    i1 = Intersection(1, s)
    i2 = Intersection(2, s)
    xs = Intersections([i1, i2])
    i = xs.hit()
    self.assertEqual(i, i1)
    
  def test_hit_some_intersection_negative(self):
    s = Sphere()
    i1 = Intersection(-1, s)
    i2 = Intersection(1, s)
    xs = Intersections([i1, i2])
    i = xs.hit()
    self.assertEqual(i, i2)
  
  def test_hit_all_intersection_negative(self):
    s = Sphere()
    i1 = Intersection(-5, s)
    i2 = Intersection(-7, s)
    xs = Intersections([i1, i2])
    i = xs.hit()
    self.assertEqual(i, None)
  
  def test_hit_is_always_the_lowest_non_negative(self):
    s = Sphere()
    i1 = Intersection(5, s)
    i2 = Intersection(7, s)
    i3 = Intersection(-3, s)
    i4 = Intersection(2, s)
    xs = Intersections([i1, i2, i3, i4])
    i = xs.hit()
    self.assertEqual(i, i4)

  def test_pre_computing_state_of_an_intersection(self):
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    shape = Sphere()
    i = Intersection(4, shape)
    comps = i.prepare_computations(r)
    self.assertEqual(comps.t, i.t)
    self.assertEqual(comps.object, i.object)
    self.assertEqual(comps.point, Point(0, 0, -1))
    self.assertEqual(comps.eyev, Vector(0, 0, -1))
    self.assertEqual(comps.normalv, Vector(0, 0, -1))

  def test_hit_intersections_occurs_on_the_outside(self):
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    shape = Sphere()
    i = Intersection(4, shape)
    comps = i.prepare_computations(r)
    self.assertEqual(comps.inside, False)
  
  def test_hit_intersections_occurs_on_the_inside(self):
    r = Ray(Point(0, 0, 0), Vector(0, 0, 1))
    shape = Sphere()
    i = Intersection(1, shape)
    comps = i.prepare_computations(r)
    self.assertEqual(comps.point, Point(0, 0, 1))
    self.assertEqual(comps.eyev, Vector(0, 0, -1))
    self.assertEqual(comps.inside, True)
    self.assertEqual(comps.normalv, Vector(0, 0, -1))
    
  def test_hit_should_offset_the_point(self):
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    shape = Sphere()
    shape.set_transform(Translation(0, 0, 1))
    i = Intersection(5, shape)
    comps = i.prepare_computations(r)
    self.assertEqual(comps.over_point.z < -EPSILON/2 and comps.point.z > comps.over_point.z
                     ,True)