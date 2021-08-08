from gr_genregraph import GenreGraph
from game_database_sep import genre_sample, special_sample
from gr_node import GameNode
from math import inf


# hashmap used to created linked lists from all the games using genre's as the keys

class GraphHashmap:

  def __init__(self, name):
    self.name = name
    self.hash_list = []
    self.max_size = 0

  def __repr__(self):
    return (f"llH - {self.name}")


  # hashmap encoder
  def hash(self, key):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code

  def compressor(self, key, collision=0):
    return (key + collision) % self.max_size


  # fills the hashmap with GenreGraphs named and sorted to match the sample dictionary's keys
  def create_graphs(self, genre_dict):
    if isinstance(genre_dict, dict) == False:
      print(f"Hashmap - {self.name} - requires a dictionary to create its linked lists")
      return

    self.max_size = len(list(genre_dict.keys()))
        
    #for i in range(self.max_size):
    #  self.hash_list.append(None)

    self.hash_list = [None for i in range(self.max_size)]

    for j in range(self.max_size):
      self.set_node(list(genre_dict.keys())[j], GenreGraph(list(genre_dict.keys())[j]))

    # self.hash_list = [self.set_node(list(genre_dict.keys())[j], GenreGraph(list(genre_dict.keys())[j])) for j in range(self.max_size)]


  # adds nodes to graphs game_lists, sorting and threshhold requirements are handled in the GenreGraph file
  # just because a node is attempting to be added here doesn't mean the graph will allow it.
  def set_node(self, key, new_node, threshhold=None):
    current_idx = self.compressor(self.hash(key))
    current_graph = self.hash_list[current_idx]
    collision = 0

    while collision != self.max_size:

      # this first if is only used to populate the hashmap with Graphs, so the new_node is actually a new graph.
      # the argument is just being repurposed
      if current_graph == None:
        self.hash_list[current_idx] = [key, new_node]
        return

      # this actually adds a new node to the graph's graph list
      elif current_graph[0] == key:
        if threshhold == None:
          current_graph[1].add_node(new_node)

          return

        else:
          current_graph[1].add_node(new_node, threshhold)
          
          return

      else:
        collision += 1
        current_idx = self.compressor(self.hash(key), collision)
        current_graph = self.hash_list[current_idx]

    print(f"Hashmap {self.name} doesn't contain a graph with that name")
    return



  # GET VARIOUS LISTS

  # returns a single GenreGraph based on the key provided
  # hasn't been turned into printable list form yet.
  def get_single_graph(self, key):
    current_idx = self.compressor(self.hash(key))
    current_graph = self.hash_list[current_idx]
    collision = 0

    while collision != self.max_size:
      if current_graph == None:
        print(f"Hashmap {self.name} doesn't contain a graph with that name")
        return None

      elif current_graph[0] == key:
        return current_graph[1]

      else:
        collision += 1
        current_idx = self.compressor(self.hash(key), collision)
        current_graph = self.hash_list[current_idx]

    print(f"Hashmap {self.name} doesn't contain a graph with that name")
    return None


  # gets only the graphs with keys that match the users main preferences
  # returns a dictionary with genre as keys and their printable versions of graphs as values 
  def get_all_lists(self, user_key_list, nodes = True, max_list_size = inf):
    all_genres_dict = {}

    for key in user_key_list:
      
      single_graph = self.get_single_graph(key)      
      all_genres_dict[key] = single_graph.create_list(nodes, max_list_size)
     
      
    # returns a dictionary of the sortable, tuple lists returned from create_list when nodes is False
    # {genre:[(genre percent, node), (genre percent, node)...], genre: [...]...}
    # debug - print(f"get_all_lists --- {all_genres_dict}")

    return all_genres_dict


  # get lists similar to dictionary functions
  def get_key_list(self):

    hash_keys = []

    for i in range(len(self.hash_list)):
      if self.hash_list[i] != None:
        hash_keys.append(self.hash_list[i][0])

    # returns an unsorted list of all fill hashmap keys - skipping empty slots - [key, key,...]
    return hash_keys

  def get_value_list(self):

    hash_values = []

    for i in range(len(self.hash_list)):
      if self.hash_list[i] != None:
        hash_values.append(self.hash_list[i][1])

    # returns only the values - skipping empty slots - [value, value,...]
    return hash_values

  def get_item_list(self, no_zero=False):

    hash_keys = []

    for i in range(len(self.hash_list)):
      if self.hash_list[i] != None:
        if no_zero == True:
          if self.hash_list[i][1] != 0:
            hash_keys.append((self.hash_list[i][1], self.hash_list[i][0]))
        else:
          hash_keys.append((self.hash_list[i][1], self.hash_list[i][0]))

    # returns a list of sortable tuples - [(value, key), (value, key),...]
    # if no_zero is True only (value,key) tuples with non-zero values will be returned.
    return hash_keys






