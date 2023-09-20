from tuple import *
from copy import copy
from copy import deepcopy

class Computations():
  def __init__(self, t = 0, object = None, point = None, eyev = None, normalv = None, inside = False, over_point = None):
    self.t = t
    self.object = copy(object)
    self.point = point
    self.eyev = eyev
    self.normalv = normalv
    self. inside = inside
    self.over_point = over_point


class Intersection():
  def __init__(self, t, object):
    self.t = t
    self.object = object
  
  def __eq__(self, other):
    return self.t == other.t and self.object == other.object 
  
  def prepare_computations(self, ray):
    comps = Computations()
    comps.t = self.t
    comps.object = deepcopy(self.object)
    comps.point = ray.position(self.t)
    comps.eyev = -ray.direction
    comps.normalv = comps.object.normal_at(comps.point)
    if comps.normalv.dot(comps.eyev) < 0:
      comps.inside = True
      comps.normalv = -comps.normalv
    comps.over_point = comps.point + comps.normalv * EPSILON
    return comps

class Intersections():
  def __init__(self, intersections = []):
    self.intersections = []
    if len(intersections) > 0:
      self.intersections = sorted(intersections,key=lambda x: x.t)
  
  def __getitem__(self, key):
    return self.intersections[key]

  @property
  def count(self):
    return len(self.intersections)
  
  def hit(self):
    result = None
    for intersection in self.intersections:
      if intersection.t >=0:
        result = intersection
        break
    return result
  
def intersect(sphere, ray):
    inverse_sphere_matrix = sphere.transform.inverse()
    ray2 = ray.transform(inverse_sphere_matrix)
    sphere_to_ray = ray2.origin - Point(0, 0, 0)
    a = ray2.direction.dot(ray2.direction)
    b = 2 * ray2.direction.dot(sphere_to_ray)
    c = sphere_to_ray.dot(sphere_to_ray) -1
    discriminant = pow(b, 2) -4 * a * c
    if discriminant < 0:
      return []
    else:
      root_discriminant = sqrt(discriminant)
      results = []
      results.append(Intersection((-b - root_discriminant) / (2 * a), sphere))
      results.append(Intersection((-b + root_discriminant) / (2 * a), sphere))
      results.sort(key=lambda x: x.t)
      return results

def intersect_world(world, ray):
  result = []
  for object in world.contains:
    result.extend(intersect(object, ray))
  result.sort(key=lambda x: x.t)
  return result