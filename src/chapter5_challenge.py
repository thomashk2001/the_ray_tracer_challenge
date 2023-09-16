from tuple import *
from canvas import *
from ray import *
from sphere import *
from intersections import *

ray_origin = Point(0, 0, -5)
wall_z = 10
wall_size = 7
canvas_pixel = 100
pixel_size = wall_size / canvas_pixel
half = wall_size / 2
canvas = Canvas(canvas_pixel, canvas_pixel)
color = Color(1, 0, 0)
shape = Sphere()

for y in range(canvas_pixel):
  world_y = half - pixel_size * y
  for x in range(canvas_pixel):
    world_x = -half + pixel_size * x
    position = Point(world_x, world_y, wall_z)
    direction = position - ray_origin
    direction.normalize()
    r = Ray(ray_origin, direction.normalize())
    xs = intersect(shape, r)
    if len(xs) > 0:
      i = Intersections(xs[0], xs[1])
      if i.hits():
        canvas.write_pixel(x,y,color)
canvas.save_to_disk()