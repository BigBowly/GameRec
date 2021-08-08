from random import randrange, shuffle
from gr_genregraph import GenreGraph
from gr_graphhashmap import GraphHashmap
from gr_node import GameNode
from gr_hashmap import Hashmap
from gr_quicksort import quicksort_tuple
from gr_maxheap import maxheaper
from game_database_sep import genre_sample, special_sample, genre_dict, special_dict, game_nodes
from gr_userdata import get_user_data, UserData, user_data, game_averages, unique_game_question




# shuffles the games so that theres a bit of randomness in what is recommended
# shuffles according to tiers so games that might not score high in the genre won't end up in the list unless the list is short
def game_list_shuffle(unshuffled_list, key, max_size):
  top_tier = []
  mid_tier = []
  bottom_tier = []
  
  for title in unshuffled_list:
    temp_value = title[1].genre_edges.get_value(key)
    if temp_value >= 80:
      top_tier.append(title[1])
    elif temp_value < 80 and temp_value > 50:
      mid_tier.append(title[1])
    else:
      bottom_tier.append(title[1])

  shuffle(top_tier)
  shuffle(mid_tier)
  shuffle(bottom_tier)

  unshuffled_list = top_tier + mid_tier + bottom_tier

  if len(unshuffled_list) < max_size:
    return unshuffled_list
  else:
    shuffle(unshuffled_list)
    return unshuffled_list[:max_size]


# similar shuffle only with specially tuned list structures for the dfs algorithm
def game_list_shuffle_dfs(unshuffled_list, max_size):
  top_tier = []
  mid_tier = []
  bottom_tier = []
  
  for title in unshuffled_list:
    temp_value = title[0]
    if temp_value >= 80:
      top_tier.append(title)
    elif temp_value < 80 and temp_value > 50:
      mid_tier.append(title)
    else:
      bottom_tier.append(title)

  shuffle(top_tier)
  shuffle(mid_tier)
  shuffle(bottom_tier)

  unshuffled_list = top_tier + mid_tier + bottom_tier

  if len(unshuffled_list) < max_size:
    return unshuffled_list
  else:
    shuffle(unshuffled_list)
    return unshuffled_list[:max_size]



# the math part of the algorithm
# calculates the percentages and averages according to - times the game is accessed, genre like percentage, genre hate percentage
# as the graph search runs down the paths, this keeps tabs on how often a game goes through the path queue.
def visited_tally(visited_titles, current_title, user_likes, user_hates, key):
  current_percent = current_title.genre_edges.get_value(key)
  user_hates_percent = 0

  if current_title in visited_titles.keys():
    total_percent = visited_titles[current_title][0]
    user_likes_percent = (user_likes[key]/100)

    # if the current key is in the user hates list, this will find the percentage to subtract from the total
    # to give the game less of chance of ending up in the list
    if key in user_hates.keys():
      user_hates_percent = (user_hates[key]/100)
    total_times = visited_titles[current_title][1]

    visited_titles[current_title] = [int(total_percent + (user_likes_percent * current_percent) - (user_hates_percent * current_percent)), total_times + 1]
  else:
    visited_titles[current_title] = [current_percent, 1]


# to add more games to the path queue, the current games genres are accessed, and this function will find the next usable genre key
# according to genre percentages. Takes into account likes, hates, and already visited
# the already visited only counts per depth search of each liked genre
def get_next_key(visited_keys, current_edges, user_hates):
  
  current_idx = 0

  while len(current_edges) > current_idx:
    current_key = current_edges[current_idx][1]
    if current_key in user_hates or current_key in visited_keys:
      current_idx += 1
    else:
      return current_key
    
    current_idx += 1

  return None



# BFS

# even though its labeled bfs, its a combination of bfs and dfs - dfs in the way it finishes its depth search for each liked genre
# before moving onto the next liked genre, but once the dfs is begun, it picks games based on a bfs path queue
def bfs(hashmap, user_likes, user_hates, played_games, max_search_depth=4):

  user_likes_keys = list(user_likes.keys())
  # debug - print(f"ulk - {user_likes_keys}")
  user_hates_keys = list(user_hates.keys())
  max_game_list_size = 2
  visited_titles = {}

  # debug - print(f"ulk - {user_likes_keys}")
  # debug - print(f"uhk - {user_hates_keys}")
  

  # first while loop is for the dfs search based on all user like keys
  # any truncating of the user likes list happens in gr_userdata - whatever is in user_likes list that makes it here
  # will be searched.
  while len(user_likes_keys) > 0:
    search_depth = 0
    path_queue = []
    visited_keys = []
    
    current_key = user_likes_keys.pop(0)
    visited_keys.append(current_key)
    temp_game_list = hashmap.get_single_graph(current_key).create_list(True)

    # debug - print(f"\ntgl - {current_key} - {temp_game_list}\n")

    if len(temp_game_list) < 1:
      search_depth = max_search_depth
    else:
      temp_game_list = game_list_shuffle(temp_game_list, current_key, max_game_list_size)
      path_queue.append([temp_game_list, 1])

    # debug - print(f"ck - {current_key} - {path_queue}\n")
  
    # breadth search portion - fans out from each games secondary, tertiary,. . . genre percentage until the
    # max depth is reached or the path_queue is empty
    while len(path_queue) > 0:
      search_col = len(path_queue)
      current_path = path_queue.pop(0)
      current_titles = current_path[0]
      search_depth = current_path[1]

      if search_depth >= max_search_depth:
        break

      for title in current_titles:
  
        visited_tally(visited_titles, title, user_likes, user_hates, current_key)

        temp_list = []
        current_title_edges = title.genre_edges.get_item_list(True)
        quicksort_tuple(current_title_edges, 0, len(current_title_edges) - 1)

        # edge key is used instead of current key until the dfs search for the current user_liked genre is complete
        edge_key = get_next_key(visited_keys, current_title_edges, user_hates_keys)

        # debug - print(f"{title} - {current_title_edges}\n")

        temp_game_list = hashmap.get_single_graph(edge_key).create_list(True)

        # debug - print(f"\ntgl2 - {edge_key} - {temp_game_list}\n")

        temp_game_list = game_list_shuffle(temp_game_list, edge_key, max_game_list_size)
        path_queue.append([temp_game_list, search_depth + 1])

        # debug - print(f"ek - {edge_key} - {path_queue}\n")


  # debug - print(f"vt - {visited_titles}\n")
  # debug - print(f"played_games - {played_games}")

  for title in played_games:
    if title in list(visited_titles.keys()):
      visited_titles.pop(title)

  # debug - print(f"vt - {visited_titles}\n")

  # returns a dictionary - {title: [percent, times it was accessed],. . .}
  return visited_titles



# splits a games genres into likes and hates for heuristic comparison
def get_like_hates(temp_game, threshhold):
  temp_genre_tuple_list = temp_game.genre_edges.get_item_list(False)
  temp_likes = []
  temp_hates = []

  for item in temp_genre_tuple_list:
    if item[0] > threshhold:
      temp_likes.append(item)
    else:
      temp_hates.append(item)

  return [temp_likes, temp_hates]



def compare_heuristic(current_likes_hates, unique_likes_hates):
  current_likes = current_likes_hates[0]
  current_hates = current_likes_hates[1]
  unique_likes = unique_likes_hates[0]
  unique_hates = unique_likes_hates[1]  

  # debug - print(f"compare - current_likes - {current_likes}\n")
  # debug - print(f"compare - unique_likes - {unique_likes}\n")

  rows = []
  cols = []
  row_count = 0  

  # likes
  for i in range(len(current_likes) + 1):
    cols = []
    for j in range(len(unique_likes) + 1):
      cols.append(0)

    rows.append(cols)

  # debug - print(f"row_col - {rows}")
      

  while row_count <= len(current_likes):
    for i in range(1, len(current_likes) + 1):
      for j in range(1, len(unique_likes) + 1):

        if current_likes[i - 1][1] == unique_likes[j - 1][1]:
          rows[i][j] = 1 + rows[i-1][j-1]
        else:
          top = rows[i-1][j]
          left = rows[i][j-1]
          if left > top:
            rows[i][j] = left
          else:
            rows[i][j] = top

    row_count += 1

  # debug - print(f"row_col - {rows}")

  final_count = rows[len(current_likes)][len(unique_likes)]
  return final_count



# DFS

# takes user likes and pulls the top game from each genre list of user likes
# each games genre tags are compared to the players unique favorite game
# the title with the most matches is added to the top games list which is returned
# user hates is not used in this algorithm, its used in the bfs algorithm
def dfs(hashmap, user_likes, unique_game, played_games, threshhold = 30, max_matches = 5):

  genre_idx_dict = {}
  check_heuristic_list = {}
  user_likes_genre_dict = hashmap.get_all_lists(user_likes, True, 10)
  unique_game_likes_hates = None
  top_matching_games = []
  visited_games = [] + played_games

  # debug - print(f"user_likes ---> {user_likes}")

  # debug - for genre in user_likes_genre_dict.keys():

    # debug - print(f"user_likes_genre_dict - {genre} - {user_likes_genre_dict[genre]}\n")

  unique_game_likes_hates = get_like_hates(unique_game, threshhold)

  for genre in user_likes_genre_dict.keys():
    check_heuristic_list[genre] = None

  # adds the top non-matching game from each genre into the heuristic check list
  # the heuristic check list will compare each game to the unique_games top genres
  # the closest match will be added to top_matching_games
  for genre in user_likes_genre_dict.keys():
    check_heuristic_list[genre] = None
    genre_idx_dict[genre] = 0

    user_likes_genre_dict[genre] = game_list_shuffle_dfs(user_likes_genre_dict[genre], len(user_likes_genre_dict[genre]))

    # debug - print(f"user_likes_genre_dict - {genre} - {user_likes_genre_dict[genre]}\n")

    current_game = user_likes_genre_dict[genre][genre_idx_dict[genre]][1]

    # debug - print(f"current_game ---> {current_game}")

    while check_heuristic_list[genre] == None and genre_idx_dict[genre] < len(user_likes_genre_dict[genre]):

      # game_node_only = [game_node[1] for game_node in check_heuristic_list.values()]

      # debug - print(f"start - check_heuristic_list ---> {check_heuristic_list}")

      if current_game in check_heuristic_list.values() or current_game in visited_games:
        current_game = user_likes_genre_dict[genre][genre_idx_dict[genre]][1]
        genre_idx_dict[genre] += 1
      else:
        check_heuristic_list[genre] = current_game

  # debug - print(f"start - check_heuristic_list ---> {check_heuristic_list}")


  while len(top_matching_games) < max_matches:
    
    game_compare_totals = []

    for genre in check_heuristic_list.keys():
      current_game = check_heuristic_list[genre]
      current_game_likes_hates = None

      if current_game != None:
        current_game_likes_hates = get_like_hates(current_game, threshhold)

        # compares each games genre percentages to the players chosen favorite game
        # returns each total of matches allowing them to be compared
        # the game with the most matches, wins.
        game_compare_totals.append((compare_heuristic(current_game_likes_hates, unique_game_likes_hates), [current_game, genre]))

        # debug - print(f"compare_totals ----- {game_compare_totals}")


    if len(game_compare_totals) <= 0:
      print(f"game_compare_totals contains zero games")
      break

    # sorts the game_compare_totals so the largest comparison is in front, ready to be popped
    # adds the top_game to the top_matching_games list and readies the heuristic slot to be filled
    quicksort_tuple(game_compare_totals, 0, len(game_compare_totals) -1)

    top_game_temp = game_compare_totals.pop(0)
    top_matching_games.append(top_game_temp[1][0])
    visited_games.append(top_game_temp[1][0])
    genre = top_game_temp[1][1]
    genre_idx_dict[genre] += 1
    check_heuristic_list[genre] = None

    # debug - print(f"\nafter single run - check_heuristic_list ---> {check_heuristic_list}")
    # debug - print(f"\nafter single run - visited_games ---> {visited_games}")


    # refill the check heuristic dictionary - same as earlier only this one doesn't initialize the index or heuristic dictionary
    for genre in user_likes_genre_dict.keys():

      # last thing - changes <= to <
      while check_heuristic_list[genre] == None and genre_idx_dict[genre] < len(user_likes_genre_dict[genre]):

        current_game = user_likes_genre_dict[genre][genre_idx_dict[genre]][1]

        if current_game in check_heuristic_list.values() or current_game in visited_games:

          # debug - print(f"user_likes_genre_dict - last game - {genre} - {user_likes_genre_dict}\n")
          # debug - print(f"genre_count --- {genre} --- {genre_idx_dict[genre]}")
          # debug - print(f"visited_games --- {genre} ---- {visited_games}")
          # debug - print(f"last_current_game ---- {genre} ---- {user_likes_genre_dict[genre][genre_idx_dict[genre]]}\n")

          current_game = user_likes_genre_dict[genre][genre_idx_dict[genre]][1]
          genre_idx_dict[genre] += 1
        else:
          check_heuristic_list[genre] = current_game

    # debug - print(f"end - check_heuristic_list ---> {check_heuristic_list}")
  
  return top_matching_games




# DEBUG STUFF

#some_user_likes = {'Singleplayer': 100, 'Adventure': 91, 'Action': 74, 'Story': 63, 'Retro': 50}
#some_user_hates = {'Multiplayer': 100, 'Action': 87, 'Coop': 80, 'Splitscreen': 60, 'Sci-fi': 59, 'Simulation': 56, 'Portable': 56, 'Party': 52, 'Adventure': 52, 'Alt-Sports': 51}


#title_to_node_played_games = user_data.played_games + []
#for i in range(len(title_to_node_played_games)):
#  current_title_string = title_to_node_played_games[i]
#  current_title_node = game_nodes.get_value(current_title_string)
#  title_to_node_played_games[i] = current_title_node

#user_data2 = UserData()
#unique_game_question()
#print(f"unique_game ---> {user_data.unique_game}")

#top_match = dfs(game_averages, some_user_likes, user_data.unique_game, title_to_node_played_games, 30, 5)

#print(f"\ntop_matching_games ---> {top_match}\n")
   


  



