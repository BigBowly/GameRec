from gr_hashmap import Hashmap


# Node connected to a game title - holds edges connected to genre's with the weights being percentages
# the percentages represent how closely related the game is to the genre
# percentages are used by the graphs
# A node can be kept out of a graph if its percentage doesn't reach the threshhold

class GameNode:
  node_threshhold = .6

  def __init__(self, title):
    self.title = title
    self.genre_edges = Hashmap(self.title, 65)
    self.special_edges = Hashmap(self.title, 15)


  def __repr__(self):
    return (f"gn - {self.title}")


  # not used for now
  def add_edge(self, category, name, percent):

    if category == "genre":
      self.genre_edges.add_value(name, percent)
    if category == "special":
      self.special_edges.add_value(name, percent)


  def get_edges(self, category="genre"):

    if category == "genre":
      return self.genre_edges.get_key_list()
    elif category == "special":
      return self.special_edges.get_key_list()

    return []
    


# DEBUG CODE

#print(game_nodes.hash_list)
#print()
#print(game_nodes.get_value("Horizon Zero Dawn").genre_edges.hash_list)
#print()
#print(game_nodes.get_value("Horizon Zero Dawn").genre_sort.hash_list)
#print()
#print(game_nodes.get_value("Doom (2016)").genre_edges.hash_list)
#print(game_nodes.get_value("NBA 2K21").genre_edges.hash_list)

