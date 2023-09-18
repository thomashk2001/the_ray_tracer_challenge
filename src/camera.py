from matrix import *
from ray import *
from math import pi
from math import tan
from canvas import *
from tqdm import tqdm
class Camera():
  def __init__(self,hsize, vsize, field_of_view):
    self.hsize = hsize
    self.vsize = vsize
    self.field_of_view = field_of_view
    self.transform = identity_matrix()
    self.half_width = 0
    self.half_height = 0
    self.pixel_size = 0
    half_view = tan(self.field_of_view / 2)
    aspect = self.hsize / self.vsize
    if aspect >= 1:
      self.half_width = half_view
      self.half_height = half_view / aspect
    else:
      self.half_width = half_view * aspect
      self.half_height = half_view
    self.pixel_size = (self.half_width * 2) / self.hsize
  
  def ray_for_pixel(self, px, py):
    xoffset = (px + 0.5)* self.pixel_size
    yoffset = (py + 0.5)* self.pixel_size
    world_x = self.half_width - xoffset
    world_y = self.half_height - yoffset
    inverse = self.transform.inverse()
    pixel = inverse * Point(world_x, world_y, -1)
    origin = inverse * Point(0, 0, 0)
    direction = pixel - origin
    direction = direction.normalize()
    return Ray(origin, direction)
  
  def render(self, world):
    progress_bar = tqdm(total=self.hsize * self.vsize, desc="Processing")
    image = Canvas(self.hsize, self.vsize)
    for y in range(self.vsize):
      for x in range(self.hsize):
        ray = self.ray_for_pixel(x, y)
        color = world.color_at(ray)
        image.write_pixel(x, y, color)
        progress_bar.update(1)
    progress_bar.close()
    return image

  