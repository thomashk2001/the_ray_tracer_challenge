import unittest
from sphere import *
from ray import *
from intersections import *
from transformation import *

class TestSpheres(unittest.TestCase):
  def test_ray_intersects_sphere_two_points(self):
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    s = Sphere()
    xs = intersect(s, r)
    self.assertEqual(len(xs), 2)
    self.assertEqual(xs[0].t, 4)
    self.assertEqual(xs[1].t, 6)
    
  def test_ray_intersects_sphere_at_tangent(self):
      r = Ray(Point(0, 1, -5), Vector(0, 0, 1))
      s = Sphere()
      xs = intersect(s, r)
      self.assertEqual(len(xs), 2)
      self.assertEqual(xs[0].t, 5.0)
      self.assertEqual(xs[1].t, 5)
        
  def test_ray_misses_sphere(self):
      r = Ray(Point(0, 2, -5), Vector(0, 0, 1))
      s = Sphere()
      xs = intersect(s, r)
      self.assertEqual(len(xs), 0)
        
  def test_ray_originates_inside_sphere(self):
    r = Ray(Point(0, 0, 0), Vector(0, 0, 1))
    s = Sphere()
    xs = intersect(s, r)
    self.assertEqual(len(xs), 2)
    self.assertEqual(xs[0].t, -1)
    self.assertEqual(xs[1].t, 1)
    
  def test_sphere_behind_ray(self):
    r = Ray(Point(0, 0, 5), Vector(0, 0, 1))
    s = Sphere()
    xs = intersect(s, r)
    self.assertEqual(len(xs), 2)
    self.assertEqual(xs[0].t, -6)
    self.assertEqual(xs[1].t, -4)
    
  def test_intersect_sets_the_object_on_the_intersection(self):
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    s = Sphere()
    xs = intersect(s,r)
    self.assertEqual(len(xs), 2)
    self.assertEqual(xs[0].object, s)
    self.assertEqual(xs[1].object, s)
  
  def test_sphere_default_transformation(self):
    s = Sphere()
    self.assertEqual(s.transform, identity_matrix(4))
  
  def test_changing_sphere_transformation(self):
    s = Sphere()
    t = Translation(2, 3, 4)
    s.set_transform(t)
    self.assertEqual(s.transform, t)
    
  def test_intersect_scaled_sphere_with_ray(self):
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    s = Sphere()
    s.set_transform(Scaling(2, 2, 2))
    xs = intersect(s, r)
    self.assertEqual(len(xs), 2)
    self.assertEqual(xs[0].t, 3)
    self.assertEqual(xs[1].t, 7)
  
  def test_intersect_translated_sphere_with_ray(self):
    r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    s = Sphere()
    s.set_transform(Translation(5, 0, 0))
    xs = intersect(s, r)
    self.assertEqual(len(xs),0)
    
  def test_normal_of_sphere_at_a_point_on_x_axis(self):
    s = Sphere()
    n = s.normal_at(Point(1, 0 ,0))
    self.assertEqual(n, Vector(1, 0, 0))
    
  def test_normal_of_sphere_at_a_point_on_y_axis(self):
    s = Sphere()
    n = s.normal_at(Point(0, 1 ,0))
    self.assertEqual(n, Vector(0, 1, 0))
  
  def test_normal_of_sphere_at_a_point_on_z_axis(self):
    s = Sphere()
    n = s.normal_at(Point(0, 0 ,1))
    self.assertEqual(n, Vector(0, 0, 1))
  
  def test_normal_of_sphere_at_a_point_on_non_axial_point(self):
    s = Sphere()
    n = s.normal_at(Point(sqrt(3)/3, sqrt(3)/3, sqrt(3)/3))
    self.assertEqual(n, Vector(sqrt(3)/3, sqrt(3)/3, sqrt(3)/3))
  
  def test_normal_is_normalized_vector(self):
    s = Sphere()
    n = s.normal_at(Point(sqrt(3)/3, sqrt(3)/3, sqrt(3)/3))
    self.assertEqual(n, n.normalize())
  
  def test_normal_on_translated_sphere(self):
    s = Sphere()
    s.set_transform(Translation(0, 1, 0))
    n = s.normal_at(Point(0, 1.70711, -0.70711))
    self.assertEqual(n, Vector(0, 0.70711, -0.70711))
  
  def test_normal_on_transformed_sphere(self):
    s = Sphere()
    m = Scaling(1, 0.5, 1) * RotationZ(pi/5)
    s.set_transform(m)
    n = s.normal_at(Point(0, sqrt(2)/2, -sqrt(2)/2))
    self.assertEqual(n, Vector(0, 0.97014, -0.24254))
  
  def test_sphere_has_default_material(self):
    s = Sphere()
    m = s.material
    self.assertEqual(m, Material())
  
  def test_sphere_has_assigned_material(self):
    s = Sphere()
    m = Material()
    m.ambient = 1
    s.material = m
    self.assertEqual(s.material, m)