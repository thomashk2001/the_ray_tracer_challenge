import unittest
from canvas import *
class TestCanvas(unittest.TestCase):
  def test_create_canvas(self):
    c = Canvas(10, 20)
    self.assertEqual(c.width, 10)
    self.assertEqual(c.height, 20)
    for row in c.canvas:
      for pixel in row:
        self.assertEqual(pixel, Color(0,0,0))
  def test_write_pixel_to_canvas(self):
    c = Canvas(10, 20)
    red = Color(1, 0, 0)
    c.write_pixel(2,3, red)
    self.assertEqual(c.pixel_at(2,3), red)
  
  def test_ppm_header(self):
    c = Canvas(5, 3)
    ppm = c.create_header().splitlines()
    header = ppm[0:3]
    expected_header = ["P3", "5 3", "255"]
    self.assertEqual(header, expected_header)
  
  def test_ppm_pixel_data(self):
    c = Canvas(5, 3)
    c1 = Color(1.5, 0, 0)
    c2 = Color(0, 0.5, 0)
    c3 = Color(-0.5, 0 ,1)
    c.write_pixel(0, 0, c1)
    c.write_pixel(2, 1, c2)
    c.write_pixel(4, 2, c3)
    ppm = c.canvas_to_ppm().splitlines()
    pixel_data = ppm[3:6]
    expected_pixel_data = [
            "255 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
            "0 0 0 0 0 0 0 128 0 0 0 0 0 0 0",
            "0 0 0 0 0 0 0 0 0 0 0 0 0 0 255",
    ]
    self.assertEqual(pixel_data, expected_pixel_data)
    
  def test_split_long_files(self):
    c = Canvas(10, 2, Color(1, 0.8, 0.6))
    ppm = c.canvas_to_ppm().splitlines()
    pixel_data = ppm[3:7]
    expected_pixel_data = [
            "255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204",
            "153 255 204 153 255 204 153 255 204 153 255 204 153",
            "255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204",
            "153 255 204 153 255 204 153 255 204 153 255 204 153"
    ]
    self.assertEqual(pixel_data, expected_pixel_data)