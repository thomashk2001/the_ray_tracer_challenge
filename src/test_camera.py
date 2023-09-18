import unittest
from camera import *
from constants import EPSILON
from transformation import *
from world import *
class TestCamera(unittest.TestCase):
  def test_constructing_camera(self):
    hsize = 160
    vsize = 120
    field_of_view = pi/2
    c = Camera(hsize, vsize, field_of_view)
    self.assertEqual(c.hsize, hsize)
    self.assertEqual(c.vsize, vsize)
    self.assertEqual(c.field_of_view, pi/2)
    self.assertEqual(c.transform, identity_matrix())
  
  def test_pixel_size_horizontal_canvas(self):
    c = Camera(200, 125, pi/2)
    self.assertEqual(abs(c.pixel_size - 0.01) < EPSILON, True)
    
  def test_pixel_size_vertical_canvas(self):
    c = Camera(125, 200, pi/2)
    self.assertEqual(abs(c.pixel_size - 0.01) < EPSILON, True)
  
  def test_constricting_ray_through_center_of_canvas(self):
    c = Camera(201, 101, pi/2)
    r = c.ray_for_pixel(100, 50)
    self.assertEqual(r.origin, Point(0, 0, 0))
    self.assertEqual(r.direction, Vector(0, 0, -1))
  
  def test_constricting_ray_through_corner_of_canvas(self):
    c = Camera(201, 101, pi/2)
    r = c.ray_for_pixel(0, 0)
    self.assertEqual(r.origin, Point(0, 0, 0))
    self.assertEqual(r.direction, Vector(0.66519, 0.33259, -0.66851))
  
  def test_constructing_ray_when_camera_is_transformed(self):
    c = Camera(201, 101, pi/2)
    c.transform = RotationY(pi/4) * Translation(0, -2, 5)
    r = c.ray_for_pixel(100, 50)
    self.assertEqual(r.origin, Point(0, 2, -5))
    self.assertEqual(r.direction, Vector(sqrt(2)/2, 0, -sqrt(2)/2))
  
  def test_rendering_wordl_with_camera(self):
    w = World()
    w.default_world()
    c = Camera(11, 11, pi/2)
    from_p = Point(0, 0,-5)
    to = Point(0, 0, 0)
    up = Vector(0, 1, 0)
    c.transform = ViewTransform(from_p, to, up)
    image = c.render(w)
    self.assertEqual(image.pixel_at(5,5), Color(0.38066, 0.47583, 0.2855))
    