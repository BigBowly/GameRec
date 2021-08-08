
# Hashmap for use by the GameNode
# doesn't use graphs, just straight key and value system to hold genre percentages
# separated the graph and node hashmaps because of import loop issues

class Hashmap:
  def __init__(self, name, max_size=10):
    self.name = name
    self.hash_list = []
    self.linked_list = False

    for i in range(max_size):
      self.hash_list.append(None)

    self.key_count = 0


  # encoder
  def hash(self, key):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code    

  def compressor(self, key_encoded, collision=0):
    return (key_encoded + collision) % len(self.hash_list)


  def check_hash_size(self):
    if self.key_count >= len(self.hash_list):
      return True
    
    return False


  def set_value(self, key, value):
    collision = 0
    encoded_index = self.compressor(self.hash(key), collision)

    if self.check_hash_size():
      print(f"No more room in hashmap - {self.name}")
      return

    while collision <= len(self.hash_list):

      if self.hash_list[encoded_index] == None:
        self.hash_list[encoded_index] = [key, value]
        self.key_count += 1
        return
      elif self.hash_list[encoded_index][0] == key:
        self.hash_list[encoded_index][1] = value
        return
      else:
        collision += 1
        encoded_index = self.compressor(self.hash(key), collision)

    return


  def get_value(self, key):
    collision = 0
    encoded_index = self.compressor(self.hash(key), collision)

    while collision <= len(self.hash_list):

      if self.hash_list[encoded_index] == None:
        print(f"{key} doesn't exist in hash - {self.name}")
        return None
      elif self.hash_list[encoded_index][0] == key:
        return self.hash_list[encoded_index][1]
      else:
        collision += 1
        encoded_index = self.compressor(self.hash(key), collision)

    return None


  def remove_value(self, key):
    collision = 0
    encoded_index = self.compressor(self.hash(key), collision)

    while collision <= len(self.hash_list):
      
      if self.hash_list[encoded_index] == None:
        print(f"{key} doesn't exist in hash - {self.name}")
        return
      elif self.hash_list[encoded_index][0] == key:
        self.hash_list[encoded_index] = None
        return
      else:
        collision += 1
        encoded_index = self.compressor(self.hash(key), collision)

    return


  # Since the hashmap (unless full) will have many "None" spots, this gathers just the keys that exist
  def get_key_list(self):

    hash_keys = []

    for i in range(len(self.hash_list)):
      if self.hash_list[i] != None:
        hash_keys.append(self.hash_list[i][0])

    return hash_keys

  def get_value_list(self):

    hash_values = []

    for i in range(len(self.hash_list)):
      if self.hash_list[i] != None:
        hash_values.append(self.hash_list[i][1])

    return hash_values

  # returns sortable tuples - no_zero will leave out any keys with 0 values
  def get_item_list(self, no_zero=False):

    hash_keys = []

    for i in range(len(self.hash_list)):
      if self.hash_list[i] != None:
        if no_zero == True:
          if self.hash_list[i][1] != 0:
            hash_keys.append((self.hash_list[i][1], self.hash_list[i][0]))
        else:
          hash_keys.append((self.hash_list[i][1], self.hash_list[i][0]))


    # returns tuple - (value, key)
    return hash_keys




# DEBUG CODE

#lefty = Hashmap("Horizon Zero Dawn", 50)

#for i in range(len(lefty.hash_list) - 2):
#  my_str = "Action " + str(i)
#  lefty.set_value(my_str, i) 

#print(lefty.hash_list)

#print(lefty.hash_list.count(None))

#print(lefty.get_value("Action"))

#lefty.remove_value("MMO")

#print(lefty.hash_list)


