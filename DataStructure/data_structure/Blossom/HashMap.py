from GivenLib.linked_list import Node, LinkedList
from GivenLib.blossom_lib import flower_definitions
class HashMap():
  def __init__(self,size):
    self.array_size = size
    self.array = [LinkedList(None) for i in range(size)]
    print('log init: ' + str(len(self.array)))
  def hash(self,key):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code
    print('log hash: ' + str(hash_code))

  def compress(self,hash_code):
    ret = hash_code % self.array_size
    print('log comp: ' + str(ret))
    return ret

  def assign(self,key,value):
    payload = Node([key,value])
    array_index = self.compress(self.hash(key))
    list_at_array = self.array[array_index]
    for item in list_at_array:
      if item[0] == key:
        item[1] = value
        return
    list_at_array.insert(payload)
    
    print('log assign: ' + str(self.array[array_index]))

  def retrieve(self,key):
    array_index = self.compress(self.hash(key))
    list_at_index = self.array[array_index]
    for item in list_at_index:
      if item[0] == key:
        return item[1]
    return None