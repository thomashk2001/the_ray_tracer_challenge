import multiprocessing
from camera import *
from world import *
from tqdm import tqdm
import os
import platform
class Data():
  def __init__(self, x,  y, camera, world):
    self.x = x
    self.y = y
    self.camera = camera
    self.world = world

def render_pixels(data):
  ray = data.camera.ray_for_pixel(data.x, data.y)
  color = world.color_at(ray)
  return(data.x, data.y, color)

def prepare_data(camera, world):
    combinations = []
    for y in range(camera.vsize):
      for x in range(camera.hsize):
        combinations.append(Data(x,y, camera, world))
    return combinations

def join_results_to_canvas(results, camera):
  progress_bar = tqdm(total=len(results), desc="Saving Image")
  image = Canvas(camera.hsize, camera.vsize)
  for result in results:
    x, y, color = result
    image.write_pixel(x, y, color)
    progress_bar.update(1)
  progress_bar.close()
  return image
def render_image(camera, world, number_of_processes):
  data = prepare_data(camera, world)
  os = platform.system()
  context_type = "fork"
  if os == 'Windows':
    context_type = "spawn"
  pool = multiprocessing.get_context(context_type).Pool(processes=number_of_processes)
  results = list(tqdm(pool.imap(render_pixels, data), total=len(data), desc="Generating Image"))
  pool.join
  pool.close()
  image = join_results_to_canvas(results, camera)
  image.save_to_disk()

  


  
  
  





from sphere import *
from world import *
from camera import *
floor = Sphere()
floor.transform = Scaling(10, 0.001, 10)
floor.material = Material()
floor.material.color = Color(1, 0.9, 0.9)
floor.material.specular = 0

left_wall = Sphere()
left_wall.transform = Translation(0, 0, 5) * RotationY(-pi/4) * RotationX(pi/2) \
                      * Scaling(10, 0.01, 10)
left_wall.material = floor.material

right_wall = Sphere()
right_wall.transform = Translation(0, 0, 5) * RotationY(pi/4) * RotationX(pi/2) \
                      * Scaling(10, 0.01, 10)
right_wall.material = floor.material

middle = Sphere()
middle.transform = Translation(-0.5, 1, 0.5)
middle.material = Material()
middle.material.color = Color(0.1, 1, 0.5)
middle.material.diffuse = 0.7
middle.material.specular = 0.3

right = Sphere()
right.transform = Translation(1.5, 0.5, -0.5) * Scaling(0.5, 0.5, 0.5)
right.material = Material()
right.material.color = Color(0.5, 1, 0.1)
right.material.diffuse = 0.7
right.material.specular = 0.3


left = Sphere()
left.transform = Translation(-1.5, 0.33, -0.55) * Scaling(0.33, 0.33, 0.33)
left.material = Material()
left.material.color = Color(1, 0.8, 0.1)
left.material.diffuse = 0.7
left.material.specular = 0.3

world = World()
world.contains = [floor, left_wall, right_wall, middle, left, right]
world.lights = [Light(Point(-10, 10, -10), Color(1, 1, 1))]

camera = Camera(2560,1440, pi/3)
camera.transform = ViewTransform(Point(0, 1.5, -5), Point(0, 1, 0), Vector(0, 1, 0))

render_image(camera,world,multiprocessing.cpu_count())

