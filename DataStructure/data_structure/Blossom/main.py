from HashMap import HashMap
from GivenLib.blossom_lib import flower_definitions
blossom = HashMap(len(flower_definitions))
for b in flower_definitions:
  blossom.assign(b[0],b[1])

print(blossom.retrieve('daisy'))
