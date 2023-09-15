from tuple import *
from copy import copy

class Intersection():
  def __init__(self, t, object):
    self.t = t
    self.object = object
  
  def __eq__(self, other):
    return self.t == other.t and self.object == other.object 

class Intersections():
  def __init__(self, *intersections):
    # uses tuple, if necessary change to list by copying each item one by one to list.
    self.intersections = sorted(intersections,key=lambda x: x.t)
  
  def __getitem__(self, key):
    return self.intersections[key]

  @property
  def count(self):
    return len(self.intersections)
  
  def hits(self):
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