from game_database_sep import genre_sample, special_sample, genre_dict, special_dict, game_nodes
from gr_genregraph import GenreGraph
from gr_graphhashmap import GraphHashmap
from gr_node import GameNode
from gr_hashmap import Hashmap


# originally used by multiple files, now these functions are only used by gr_userdata


# function for populating graphs with game titles - for right now, will only populate graphs that match user's likes
def create_graph_lists(hashmap, user_keys, uniquekey=None, new_threshhold=70, min_game_list_size=3): 
  if uniquekey == None:
    for title in game_nodes.get_key_list():
      # change user_prefs to genre_sample to populate all possible genre tags
      for key in user_keys.keys():

        hashmap.get_single_graph(key).change_threshhold(new_threshhold)
        hashmap.set_node(key, game_nodes.get_value(title))


  # this part will allow individual genre graphs to be reevaluated based on a lower threshhold to make sure a list has a min # of games
  else:
    threshhold = new_threshhold
    unique_graph_length = len(hashmap.get_single_graph(uniquekey).game_list)

    while threshhold > 10 and unique_graph_length < min_game_list_size:
      threshhold -= 10
      hashmap.get_single_graph(uniquekey).game_list = []
      
      for title in game_nodes.get_key_list():

        hashmap.set_node(uniquekey, game_nodes.get_value(title), threshhold)



# checks the length of each genre graphs game list and will call the create_graph_list function again on specific genre graphs
# for them to be reevaluated until they have the required number of games or the threshhold reaches 0
# (meaning whatever list you have at the end is the max number possible)
def check_graph_length(hashmap, user_keys, min_game_list_size=3):
  temp_dict = hashmap.get_all_lists(list(user_keys.keys()))

  for key in temp_dict.keys():

    # debug - print(f"{key} --- {len(temp_dict[key])}")

    if len(temp_dict[key]) < min_game_list_size:
      create_graph_lists(hashmap, genre_sample, key, 70, min_game_list_size)
