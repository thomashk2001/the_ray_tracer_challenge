import unittest
from transformation import *
from tuple import *
class TestTransformation(unittest.TestCase):
  def test_multiply_translation_matrix(self):
    transform = Translation(5, -3, 2)
    p = Point(-3, 4, 5)
    self.assertEqual(transform * p, Point(2, 1, 7))
  
  def test_multiply_inverse_translation_matrix(self):
    transform = Translation(5, -3, 2)
    inv = transform.inverse()
    p = Point(-3, 4, 5)
    self.assertEqual(inv * p, Point(-8, 7, 3))
  
  def test_translation_does_not_affect_vector(self):
    transform = Translation(5, -3, 2)
    v = Vector(-3, 4, 5)
    self.assertEqual(transform * v, Vector(-3, 4, 5))
  
  def test_scaling_matrix_applied_point(self):
    transform = Scaling(2, 3, 4)
    p = Point(-4, 6, 8)
    self.assertEqual(transform * p, Point(-8, 18, 32))
    
  def test_scaling_matrix_applied_vector(self):
    transform = Scaling(2, 3, 4)
    v = Vector(-4, 6, 8)
    self.assertEqual(transform * v, Vector(-8, 18, 32))
  
  def test_multiply_inverse_scaling_matrix(self):
    transform = Scaling(2, 3, 4)
    inv = transform.inverse()
    v = Vector(-4, 6, 8)
    self.assertEqual(inv * v, Vector(-2, 2, 2))
  
  def test_reflecting_by_scaling_negative_value(self):
    transform = Scaling(-1, 1, 1)
    p = Point(2, 3, 4)
    self.assertEqual(transform * p, Point(-2, 3, 4))
  
  def test_rotating_point_around_x_axis(self):
    p = Point(0, 1, 0)
    half_quarter = RotationX(pi / 4)
    full_quarter = RotationX(pi / 2)
    self.assertEqual(half_quarter * p, Point(0, sqrt(2)/2, sqrt(2)/2))
    self.assertEqual(full_quarter * p, Point(0, 0, 1))
    
  def test_inverse_rotating_around_x_axis(self):
    p = Point(0, 1, 0)
    half_quarter = RotationX(pi / 4)
    inv = half_quarter.inverse()
    self.assertEqual(inv * p, Point(0, sqrt(2)/2, -sqrt(2)/2))
  
  def test_rotating_point_around_y_axis(self):
    p = Point(0, 0, 1)
    half_quarter = RotationY(pi / 4)
    full_quarter = RotationY(pi / 2)
    self.assertEqual(half_quarter * p, Point(sqrt(2)/2, 0, sqrt(2)/2))
    self.assertEqual(full_quarter * p, Point(1, 0, 0))
    
  def test_rotating_point_around_z_axis(self):
    p = Point(0, 1, 0)
    half_quarter = RotationZ(pi / 4)
    full_quarter = RotationZ(pi / 2)
    self.assertEqual(half_quarter * p, Point(-sqrt(2)/2 , sqrt(2)/2, 0))
    self.assertEqual(full_quarter * p, Point(-1, 0, 0))
  
  def test_shearing_x_in_proportion_to_y(self):
    transform = Shearing(x_y = 1)
    p = Point(2, 3, 4)
    self.assertEqual(transform * p, Point(5, 3, 4))
    
  def test_shearing_x_in_proportion_to_z(self):
    transform = Shearing(x_z = 1)
    p = Point(2, 3, 4)
    self.assertEqual(transform * p, Point(6, 3, 4))
    
  def test_shearing_y_in_proportion_to_x(self):
    transform = Shearing(y_x = 1)
    p = Point(2, 3, 4)
    self.assertEqual(transform * p, Point(2, 5, 4))
    
  def test_shearing_y_in_proportion_to_z(self):
    transform = Shearing(y_z = 1)
    p = Point(2, 3, 4)
    self.assertEqual(transform * p, Point(2, 7, 4))
    
  def test_shearing_z_in_proportion_to_x(self):
    transform = Shearing(z_x = 1)
    p = Point(2, 3, 4)
    self.assertEqual(transform * p, Point(2, 3, 6))

  def test_shearing_z_in_proportion_to_y(self):
    transform = Shearing(z_y = 1)
    p = Point(2, 3, 4)
    self.assertEqual(transform * p, Point(2, 3, 7))
  
  def test_individual_transformations(self):
    p = Point(1, 0, 1)
    A = RotationX(pi / 2)
    B = Scaling(5, 5, 5)
    C = Translation(10, 5, 7)
    p2 = A * p
    self.assertEqual(p2, Point(1, -1, 0))
    p3 = B * p2
    self.assertEqual(p3, Point(5, -5, 0))
    p4 = C * p3
    self.assertEqual(p4, Point(15, 0, 7))
    
  def test_chained_transformations(self):
    p = Point(1, 0, 1)
    A = RotationX(pi / 2)
    B = Scaling(5, 5, 5)
    C = Translation(10, 5, 7)
    T = C * B * A * p
    self.assertEqual(T, Point(15, 0, 7))
  
  def test_transformation_matrix_default_orientation(self):
    from_p = Point(0, 0, 0)
    to = Point(0, 0, -1)
    up = Vector(0, 1, 0)
    t = ViewTransform(from_p, to, up)
    self.assertEqual(t, identity_matrix(4))
    
  def test_view_transformation_matrix_looking_in_positive_z_direction(self):
    from_p = Point(0, 0, 0)
    to = Point(0, 0, 1)
    up = Vector(0, 1, 0)
    t = ViewTransform(from_p, to, up)
    self.assertEqual(t, Scaling(-1, 1, -1))
    
  def test_view_transformation_moves_the_world(self):
    from_p = Point(0, 0, 8)
    to = Point(0, 0, 0)
    up = Vector(0, 1, 0)
    t = ViewTransform(from_p, to, up)
    self.assertEqual(t, Translation(0, 0, -8))
    
  def test_arbitrary_view_transformation(self):
    from_p = Point(1, 3, 2)
    to = Point(4, -2, 8)
    up = Vector(1, 1, 0)
    t = ViewTransform(from_p, to, up)
    expected = Matrix(size= 4)
    expected.matrix = [
      [-0.50709, 0.50709, 0.67612, -2.36643],
      [0.76772, 0.60609, 0.12122, -2.82843],
      [-0.35857, 0.59761, -0.71714, 0.00000],
      [0.00000, 0.00000, 0.00000, 1.00000]
    ]
    self.assertEqual(t, expected)
    
    
