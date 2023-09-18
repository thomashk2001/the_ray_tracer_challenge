from sphere import *
from light import *
from tuple import *
from transformation import *
from ray import *
from intersections import *
class World():
  def __init__(self):
    self.contains = []
    self.lights = []
  
  def default_world(self):
    light = Light(Point(-10, 10, -10), Color(1, 1, 1))
    s1 = Sphere()
    s1.material = Material(Color(0.8, 1, 0.6), diffuse= 0.7, specular= 0.2)
    s2 = Sphere()
    s2.set_transform(Scaling(0.5, 0.5, 0.5))
    self.contains.extend((s1, s2))
    self.lights.append(light)

  def shade_hit(self, comps):
    result_color = Color(0, 0, 0)
    material = comps.object.material
    point = comps.point
    eyev = comps.eyev
    normalv = comps.normalv
    for light in self.lights:
      result_color += lighting(material, light, point, eyev, normalv)
    return result_color
  
  def color_at(self, ray):
    result_color = Color(0, 0, 0)
    intersections = intersect_world(self, ray)
    intersections = Intersections(intersections)
    hit = intersections.hits()
    if hit:
      comps = hit.prepare_computations(ray)
      result_color = self.shade_hit(comps)
    return result_color



# w = World()
# w.default_world()
# r = Ray(Point(0, 0, -5), Vector(0, 1, 0))
# c = w.color_at(r)
# self.assertEqual(c, Color(0, 0, 0))