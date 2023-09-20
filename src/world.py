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
    point = comps.over_point
    eyev = comps.eyev
    normalv = comps.normalv
    for light in self.lights:
      is_shadowed = self.is_shadowed(point, light)
      result_color += lighting(material, light, point, eyev, normalv, is_shadowed)
    return result_color
  
  def color_at(self, ray):
    result_color = Color(0, 0, 0)
    intersections = intersect_world(self, ray)
    intersections = Intersections(intersections)
    hit = intersections.hit()
    if hit:
      comps = hit.prepare_computations(ray)
      result_color = self.shade_hit(comps)
    return result_color
  
  # TODO: TEST IF THIS FUNCTIONS WORKS WITH MULTIPLE LIGHT SOURCES
  def is_shadowed(self, point, light):
    result = False
    v = light.position - point
    distance = v.magnitude()
    direction = v.normalize()
    r = Ray(point, direction)
    intersections = intersect_world(self, r)
    intersections = Intersections(intersections)
    h = intersections.hit()
    if h and h.t < distance:
      result = True
    else:
      result = False
    return result
      