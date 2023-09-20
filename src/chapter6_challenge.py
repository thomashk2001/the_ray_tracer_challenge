from tuple import *
from canvas import *
from ray import *
from sphere import *
from intersections import *
from light import *
from tqdm import tqdm

ray_origin = Point(0, 0, -5)
wall_z = 10
wall_size = 7
canvas_pixel = 1000
pixel_size = wall_size / canvas_pixel
half = wall_size / 2
canvas = Canvas(canvas_pixel, canvas_pixel)
color = Color(1, 0, 0)
shape = Sphere()

shape.material = Material(color=Color(1, 0.2, 1))
light_position = Point(-10, 10, -10)
light_color = Color(1, 1, 1)
light = Light(light_position, light_color)


progress_bar = tqdm(total=canvas_pixel * canvas_pixel, desc="Processing")


for y in range(canvas_pixel):
  world_y = half - pixel_size * y
  for x in range(canvas_pixel):
    world_x = -half + pixel_size * x
    position = Point(world_x, world_y, wall_z)
    direction = position - ray_origin
    r = Ray(ray_origin, direction.normalize())
    xs = intersect(shape, r)
    if len(xs) > 0:
      i = Intersections([xs[0], xs[1]])
      intersection =  i.hit()
      point = r.position(intersection.t)
      normal = intersection.object.normal_at(point)
      eye = -r.direction
      color = lighting(intersection.object.material, light, point, eye, normal)
      canvas.write_pixel(x,y,color)
    progress_bar.update(1)
canvas.save_to_disk()
progress_bar.close()

print("Image export ended!")