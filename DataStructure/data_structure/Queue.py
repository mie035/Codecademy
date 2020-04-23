from node import Node

class Queue:
  def __init__(self, head = None, tail = None, max_size=None):
    self.head = head
    self.tail = tail
    self.max_size = max_size
    self.size = 0
    
  # Add your enqueue method below:
  def enqueue(self,value):
    if self.has_space():
      item_to_add = Node(value)
      print("Adding " + str(item_to_add.get_value()+" to the queue!"))
      if self.get_size()==0:
        self.head = item_to_add
        self.tail = item_to_add
      else:
        self.tail.set_next_node(item_to_add)
        self.tail = item_to_add
        self.size += 1
    else:
      print("cannot enqueue!")
  def peek(self):
    if self.is_empty():
      print("Nothing to see here!")
    else:
      return self.head.get_value()
  
  def get_size(self):
    return self.size
  
  def has_space(self):
    if self.max_size == None:
      return True
    else:
      return self.max_size > self.get_size()
    
  def is_empty(self):
    return self.size == 0

q = Queue()
q.enqueue("all the fluffy kitties")