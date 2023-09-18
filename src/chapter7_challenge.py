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

camera = Camera(500, 250, pi/3)
camera.transform = ViewTransform(Point(0, 1.5, -5), Point(0, 1, 0), Vector(0, 1, 0))

canvas = camera.render(world)
canvas.save_to_disk()
