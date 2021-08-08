from gr_node import GameNode
from gr_hashmap import Hashmap
from game_database_sep import genre_dict, special_dict, genre_sample, special_sample
# from gr_quicksort import quicksort
from math import inf
from random import choice


# replaced Linked Lists with Graphs since I can have single instance nodes in any order within the graph lists

class GenreGraph:
  main_threshhold = 70

  def __init__(self, genre):
    self.genre = genre
    self.game_list = []
    self.sorted_game_list = []
    self.threshhold = GenreGraph.main_threshhold


  def change_threshhold(self, new_threshhold):
    self.threshhold = new_threshhold


  # adds nodes to the genregraph's game list in descending order according to the genre name of the graph
  def add_node(self, new_game, threshhold=None):

    if threshhold == None:
      threshhold = self.threshhold

    # debug - if isinstance(new_game, GameNode) != True:
      # debug - print(f"Use existing GameNode")
      # debug - return

    new_game_value = new_game.genre_edges.get_value(self.genre)

    # debug - if new_game_value < threshhold:
      # debug - print(f"{new_game.title} doesn't meet the threshhold for the {self.genre} graph.")
      # debug - return

    if len(self.game_list) == 0:
      self.game_list.append(new_game)

      # debug - print(f"self.game_list - {self.genre} -  {self.game_list}")

      return

    for i in range(len(self.game_list)):
      current_game_value = self.game_list[i].genre_edges.get_value(self.genre)

      # debug - print(f"ngv - {new_game}, {new_game_value}  >=  cgv - {self.game_list[i]}, {current_game_value}")

      if new_game_value >= current_game_value:
        self.game_list.insert(i, new_game)

        # debug - print(f"self.game_list - {self.genre} -  {self.game_list}")

        return

    self.game_list.append(new_game)

    # debug - print(f"self.game_list - {self.genre} -  {self.game_list}")

    return


  # function that makes it possible to resort the game_list using whatever metric is in the sorting samples
  # not used that I know of
  
  #def re_sort(self, sort_value):
  #  self.sorted_game_list = self.game_list + []
  #  quicksort(self.sorted_game_list, 0, len(self.sorted_game_list) - 1, self.genre)


  # creates a list with values and titles, or returns the normal - node only - version of game_list
  def create_list(self, nodes=True, size=inf):

    game_list = []

    if nodes == True:
      if size == inf:
        for node in self.game_list:
          game_list.append((node.genre_edges.get_value(self.genre), node))
        # return self.game_list

      else:
        if size > len(self.game_list):
          size = len(self.game_list)
        for i in range(size):
          game_list.append((self.game_list[i].genre_edges.get_value(self.genre), self.game_list[i]))
        # return self.game_list[:size]

    else:
      if len(self.game_list) < size:
        for node in self.game_list:
          game_list.append((node.genre_edges.get_value(self.genre), node.title))

      else:
        if size > len(self.game_list):
          size = len(self.game_list)
        for i in range(size):
          game_list.append((self.game_list[i].genre_edges.get_value(self.genre), self.game_list[i].title))


    # returns a list of sortable tuples - [(genre percent, game node)...] - if nodes=True a GameNode will be returned
    # otherwise the nodes string title is returned.

    # debug - print(f"\ngame_list ---- {game_list}\n")

    return game_list



    






# DEBUG CODE

#game_nodes = Hashmap("Game Nodes", 100)

## creates and adds GameNode to game_nodes
#for title in genre_dict:
#  # game_nodes.append(GameNode(game_dict[game_dict.keys()[i]]))

#  game_nodes.set_value(title, GameNode(title)) 

#  # takes the edge and weight values(percentages) and addes them to the GameNodes edge hashmap
#  for genre in genre_dict[title]:
    
#    game_nodes.get_value(title).genre_edges.set_value(genre, genre_dict[title][genre])
  
#  for special in special_dict[title]:

#    game_nodes.get_value(title).special_edges.set_value(special, special_dict[title][special])



#lefty = GenreGraph("FPP")

#lefty.add_node(game_nodes.get_value("Doom (2016)"))




