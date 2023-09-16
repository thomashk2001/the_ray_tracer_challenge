from tuple import Color
from copy import copy
class Canvas():
  def __init__(self, width, height, color = Color(0,0,0)):
    self.width = width
    self.height = height
    canvas_color = color
    self.canvas_color = canvas_color
    self.canvas = [[self.canvas_color] * width for _ in range(height)]
  
  def write_pixel(self, x, y, color):
    self.canvas[y][x] = copy(color)
  
  def pixel_at(self, x,y):
    return self.canvas[y][x]
  
  def create_header(self):
    return f"P3\n{self.width} {self.height}\n255\n"
  
  def generate_sub_list(self, list):
    sub_list_max_size = 17
    limit = len(list)
    sub_list = [list[i:i+sub_list_max_size] for i in range(0, limit, 
                                                           sub_list_max_size)]
    return sub_list
  def canvas_to_ppm(self):
    ppm_file = self.create_header()
    pixel_data = ""
    for row in self.canvas:
      ppm_temp_line = []
      for pixel in row:
        ppm_temp_line.extend(pixel.convert_to_rgb())
      splitted_ppm_temp_line = self.generate_sub_list(ppm_temp_line)
      for sub_list in splitted_ppm_temp_line:
        pixel_data += " ".join(sub_list) + "\n"
    ppm_file += pixel_data
    return ppm_file + "\n"
  
  def save_to_disk(self):
    file = open("img.ppm", "w")
    file.write(self.canvas_to_ppm())
    file.close()