import unittest
from tuple import *
class TestTuples(unittest.TestCase):
  def test_points(self):
    a = Point(4.3, -4.2, 3.1)
    self.assertIsInstance(a, Point)
    self.assertEqual(Tuple(4.3, -4.2, 3.1, 1.0), a)
      
  def test_vectors(self):
    a = Vector(4.3, -4.2, 3.1)
    self.assertIsInstance(a, Vector)
    self.assertEqual(Tuple(4.3, -4.2, 3.1, 0.0), a)
    
  def test_add(self):
    a1 = Point(3, -2, 5)
    a2 = Vector(-2, 3, 1)
    r = a1+a2
    self.assertEqual(Tuple(1, 1, 6, 1), r)
    
  def test_sub_points(self):
    p1 = Point(3, 2, 1)
    p2 = Point(5, 6, 7)
    r = p1-p2
    self.assertIsInstance(r, Vector)
    self.assertEqual(Vector(-2,-4,-6), r)
  
  def test_sub_vector_point(self):
    p = Point(3, 2, 1)
    v = Vector(5, 6, 7)
    r = p - v
    self.assertIsInstance(r,Point)
    self.assertEqual(Point(-2,-4,-6),r)
    
  def test_sub_vectors(self):
    v1 = Vector(3, 2, 1)
    v2 = Vector(5, 6, 7)
    r = v1 - v2
    self.assertIsInstance(r,Vector)
    self.assertEqual(Vector(-2,-4,-6),r)
    
  def test_sub_vector_zero_vector(self):
    v1 = Vector(0,0,0,0)
    v2 = Vector(1, -2, 3)
    r = v1 - v2
    self.assertIsInstance(r, Vector)
    self.assertEqual(Vector(-1, 2, -3),r)
  
  def test_negate_tuple(self):
    a = Tuple(1, -2, 3, 0)
    r = -a
    self.assertEqual(Tuple(-1, 2, -3, 0), r)
  
  def test_multiplication_tuple_scalar(self):
    a = Tuple(1, -2, 3, -4)
    r = a * 3.5
    self.assertEqual(Tuple(3.5, -7, 10.5, -14), r)
  
  def test_multiplication_tuple_fraction(self):
    a = Tuple(1, -2, 3, -4)
    r = a * 0.5
    self.assertEqual(Tuple(0.5, -1, 1.5, -2), r)
  
  def test_division_tuple_scalar(self):
    a = Tuple(1, -2, 3, -4)
    r = a / 2
    self.assertEqual(Tuple(0.5, -1, 1.5, -2), r)
    
  def test_magnitud_100(self):
    v = Vector(1, 0, 0)
    self.assertEqual(v.magnitude(), 1)
    
  def test_magnitud_010(self):
    v = Vector(0, 0, 1)
    self.assertEqual(v.magnitude(), 1)
  
  def test_magnitud_001(self):
    v = Vector(0, 1, 0)
    self.assertEqual(v.magnitude(), 1)
    
  def test_magnitud_123(self):
    v = Vector(1,2,3)
    self.assertEqual(v.magnitude(), sqrt(14))
    
  def test_magnitud_neg123(self):
    v = Vector(-1,-2,-3)
    self.assertEqual(v.magnitude(), sqrt(14))
  
  def test_normalize_vector_400(self):
    v = Vector(4, 0 , 0)
    self.assertEqual(v.normalize(), Vector(1,0,0))
    
  def test_normalize_vector_123(self):
    v = Vector(1, 2 , 3)
    self.assertEqual(v.normalize(), Vector(0.26726, 0.53452, 0.80178))
  
  def test_normalized_vector_magnitud(self):
    v = Vector(1, 2 , 3)
    norm = v.normalize()
    self.assertEqual(norm.magnitude(), 1)
  
  def test_dot(self):
    a = Vector(1, 2 , 3)
    b = Vector(2,3,4)
    self.assertEqual(a.dot(b), 20)
  
  def test_cross(self):
    a = Vector(1, 2, 3)
    b = Vector( 2, 3, 4)
    self.assertEqual(a.cross(b), Vector(-1, 2, -1))
    self.assertEqual(b.cross(a), Vector(1, -2, 1))
    
  def test_color_base(self):
    c = Color(-0.5, 0.4, 1.7)
    self.assertEqual(c.red, -0.5)
    self.assertEqual(c.green, 0.4)
    self.assertEqual(c.blue, 1.7)
  
  def test_add_colors(self):
    c1= Color(0.9, 0.6, 0.75)
    c2 = Color(0.7, 0.1, 0.25)
    r = c1 + c2
    self.assertEqual(r, Color(1.6, 0.7, 1.0))
  
  def test_sub_colors(self):
    c1= Color(0.9, 0.6, 0.75)
    c2 = Color(0.7, 0.1, 0.25)
    r = c1 - c2
    self.assertEqual(r, Color(0.2, 0.5, 0.5))
    
  def test_multiply_color_scalar(self):
    c1 = Color(0.2, 0.3, 0.4)
    r = c1 * 2
    self.assertEqual(r, Color(0.4, 0.6, 0.8))
    
  def test_multiply_colors(self):
    c1 = Color(1, 0.2, 0.4)
    c2 = Color(0.9, 1, 0.1)
    r = c1 * c2
    self.assertEqual(r, Color(0.9, 0.2, 0.04))
  
  def test_reflecting_vector_at_45(self):
    v = Vector(1, -1, 0)
    n = Vector(0, 1, 0)
    r = v.reflect(n)
    self.assertEqual(r, Vector(1, 1, 0))
  
  def test_reflecting_vector_off_slanted_surface(self):
    v = Vector(0, -1, 0)
    n = Vector(sqrt(2)/2, sqrt(2)/2, 0)
    r = v.reflect(n)
    self.assertEqual(r, Vector(1, 0 , 0))
