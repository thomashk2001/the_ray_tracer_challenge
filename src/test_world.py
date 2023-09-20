import unittest
from world import *
from intersections import *
class TestWorld(unittest.TestCase):
  def test_creating_world(self):
    w = World()
    self.assertEqual(len(w.contains), 0)
    self.assertEqual(len(w.lights), 0)
    
  def test_default_world(self):
    light = Light(Point(-10, 10, -10), Color(1, 1, 1))
    s1 = Sphere()
    s1.material = Material(Color(0.8, 1, 0.6), diffuse= 0.7, specular= 0.2)
    s2 = Sphere()
    s2.set_transform(Scaling(0.5, 0.5, 0.5))
    w = World()
    w.default_world()
    self.assertEqual(w.lights[0], light)
    self.assertEqual(s1 in w.contains,True)
    self.assertEqual(s2 in w.contains,True)
  
  def test_intersect_world_ray(self):
    w = World()
    w.default_world()
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    xs = intersect_world(w, r)
    self.assertEqual(len(xs), 4)
    self.assertEqual(xs[0].t, 4)
    self.assertEqual(xs[1].t, 4.5)
    self.assertEqual(xs[2].t, 5.5)
    self.assertEqual(xs[3].t, 6)
  
  def test_shading_an_intersection(self):
    w = World()
    w.default_world()
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    shape = w.contains[0]
    i = Intersection(4, shape)
    comps = i.prepare_computations(r)
    c = w.shade_hit(comps)
    self.assertEqual(c, Color(0.38066, 0.47583, 0.2855))
  
  def test_shading_intersection_from_the_inside(self):
    w = World()
    w.default_world()
    w.lights[0] = Light(Point(0, 0.25, 0), Color(1, 1, 1))
    r = Ray(Point(0, 0, 0), Vector(0, 0, 1))
    shape = w.contains[1]
    i = Intersection(0.5, shape)
    comps = i.prepare_computations(r)
    c = w.shade_hit(comps)
    self.assertEqual(c, Color(0.90498, 0.90498, 0.90498))
  
  def test_color_ray_misses(self):
    w = World()
    w.default_world()
    r = Ray(Point(0, 0, -5), Vector(0, 1, 0))
    c = w.color_at(r)
    self.assertEqual(c, Color(0, 0, 0))
  
  def test_color_ray_hits(self):
    w = World()
    w.default_world()
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    c = w.color_at(r)
    self.assertEqual(c, Color(0.38066, 0.47583, 0.2855))
    
  def test_color_with_intersection_behind_the_ray(self):
    w = World()
    w.default_world()
    outer = w.contains[0]
    outer.material.ambient = 1
    inner = w.contains[1]
    inner.material.ambient = 1
    r = Ray(Point(0, 0, 0.75), Vector(0, 0, -1))
    c = w.color_at(r)
    self.assertEqual(c, inner.material.color)
  def test_no_shadow_when_nothing_is_colinear_with_point_light(self):
    w = World()
    w.default_world()
    p = Point(0, 10, 0)
    self.assertEqual(w.is_shadowed(p, w.lights[0]), False)
    
  def test_shadow_when_object_is_between_point_light(self):
    w = World()
    w.default_world()
    p = Point(10, -10, 10)
    self.assertEqual(w.is_shadowed(p, w.lights[0]), True)
  
  def test_no_shadow_when_object_is_behind_light(self):
    w = World()
    w.default_world()
    p = Point(-20, 20, -20)
    self.assertEqual(w.is_shadowed(p, w.lights[0]), False)
  
  def test_no_shadow_when_object_is_behind_point(self):
    w = World()
    w.default_world()
    p = Point(-2, 2, -2)
    self.assertEqual(w.is_shadowed(p, w.lights[0]), False)
    
  def test_shade_hit_shadow(self):
    w = World()
    w.lights.append(Light(Point(0, 0, -10), Color(1, 1, 1)))
    s1 = Sphere()
    w.contains.append(s1)
    s2 = Sphere()
    s2.set_transform(Translation(0, 0, 10))
    w.contains.append(s2)
    r = Ray(Point(0, 0, 5), Vector(0, 0, 1))
    i = Intersection(4, s2)
    comps = i.prepare_computations(r)
    c = w.shade_hit(comps)
    self.assertEqual(c, Color(0.1, 0.1, 0.1))