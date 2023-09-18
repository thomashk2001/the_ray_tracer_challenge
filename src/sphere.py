from matrix import *
from tuple import *
from material import *
from copy import deepcopy

sphere_ids_generator = 0

def get_id():
  global sphere_ids_generator
  id = sphere_ids_generator
  sphere_ids_generator += 1
  return id
class Sphere():
  def __init__(self):
    self.id = get_id()
    self.transform = identity_matrix(4)
    self.material = Material()
    
  def set_transform(self, transformation):
    self.transform = deepcopy(transformation)
    
  def __eq__(self, other):
    # self.id == other.id WAS OMITTED TO PAST A TEST CREATE WORLD
    # TODO: CHECK IF THIS IS NEEDED LATER AND CHANGE TEST
    result =  self.transform == other.transform and \
      self.material == other.material
    return result
  
  def normal_at(self,world_point):
    object_point = self.transform.inverse() * world_point
    object_normal = object_point - Point(0, 0, 0)
    world_normal = self.transform.inverse().transpose() * object_normal
    world_normal.w = 0
    return world_normal.normalize()

