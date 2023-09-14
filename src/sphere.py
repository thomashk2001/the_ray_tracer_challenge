
sphere_ids_generator = 0

def get_id():
  global sphere_ids_generator
  id = sphere_ids_generator
  sphere_ids_generator += 1
  return id
class Sphere():
  def __init__(self):
    self.id = get_id()
    
  def __eq__(self, other):
    result = self.id == other.id
    return result

