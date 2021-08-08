from gr_genregraph import GenreGraph
from gr_graphhashmap import GraphHashmap
from gr_node import GameNode
from gr_hashmap import Hashmap
from game_database_sep import genre_sample, special_sample, genre_dict, special_dict, game_nodes
from gr_userdata import get_user_data, user_data, game_averages
from gr_graphsearch import bfs, dfs
from gr_quicksort import quicksort_tuple
from gr_maxheap import maxheaper
from gr_miscfunctions import clear_screen

  

# REPETITIOUS TASKS

# take the dictionary returned by the bfs in gr_graphsearch, sorts it using a maxheap
# It leaves out any titles returned with zero percentage points.
def average_tally(tally_dict, max_size):
  final_rec_list = []

  for title,tally in tally_dict.items():
    if tally[0] <= 0:
      final_tally = 0
    else:
      final_tally = int(tally[0]/tally[1])

    maxheaper.push(final_rec_list, (final_tally, title))

  sorted_final_rec_list = maxheaper.sort_threshhold_v2(final_rec_list, 20)

  # returns a list of tuples the size of max_size - (total percent, game_node)
  if len(sorted_final_rec_list) < max_size:
    return sorted_final_rec_list
  else:
    return sorted_final_rec_list[:max_size]


# prints the recommended games lists - bfs and dfs return different lists
def print_recommend_list_genre(title_tally, bfs_dfs):

  if bfs_dfs == "bfs":

    for i in range(len(title_tally)):

      genre_list = title_tally[i][1].genre_edges.get_item_list(True)
      quicksort_tuple(genre_list, 0, len(genre_list) - 1)
      if len(genre_list) > 5:
        genre_list = genre_list[:5]

      genre_string = "    - "    
      for j in range(len(genre_list)):
        genre_string += (f" {genre_list[j][1]}, ")
      genre_string = genre_string[:-2]

      print(f" {i+1}: {title_tally[i][1].title}")
      print(genre_string)

  elif bfs_dfs == "dfs":

    for i in range(len(title_tally)):

      genre_list = title_tally[i].genre_edges.get_item_list(True)
      quicksort_tuple(genre_list, 0, len(genre_list) - 1)
      if len(genre_list) > 5:
        genre_list = genre_list[:5]

      genre_string = "    - "    
      for j in range(len(genre_list)):
        genre_string += (f" {genre_list[j][1]}, ")
      genre_string = genre_string[:-2]

      print(f" {i+1}: {title_tally[i].title}")
      print(genre_string)


def print_recommend_list_special(title_tally, sort_type, bfs_dfs):

  special_title_list = []

  if bfs_dfs == "bfs":

    for i in range(len(title_tally)):

      special_value = title_tally[i][1].special_edges.get_value(sort_type)
      if isinstance(special_value,list) == True:
        special_value = special_value[0]

      genre_list = title_tally[i][1].genre_edges.get_item_list(True)
      quicksort_tuple(genre_list, 0, len(genre_list) - 1)
      if len(genre_list) > 5:
        genre_list = genre_list[:5]

      genre_string = "    - "    
      for j in range(len(genre_list)):
        genre_string += (f" {genre_list[j][1]}, ")
      genre_string = genre_string[:-2]

      combined_tuple = (special_value, (genre_string, title_tally[i][1].title))
      special_title_list.append(combined_tuple)
      quicksort_tuple(special_title_list, 0, len(special_title_list) -1)

    for i in range(len(special_title_list)):

      print(f" {i+1}: {special_title_list[i][1][1]}")
      print(f"     - {sort_type}: {special_title_list[i][0]}")
      print(genre_string)

  if bfs_dfs == "dfs":

    for i in range(len(title_tally)):

      special_value = title_tally[i].special_edges.get_value(sort_type)
      if isinstance(special_value,list) == True:
        special_value = special_value[0]

      genre_list = title_tally[i].genre_edges.get_item_list(True)
      quicksort_tuple(genre_list, 0, len(genre_list) - 1)
      if len(genre_list) > 5:
        genre_list = genre_list[:5]

      genre_string = "    - "    
      for j in range(len(genre_list)):
        genre_string += (f" {genre_list[j][1]}, ")
      genre_string = genre_string[:-2]

      combined_tuple = (special_value, (genre_string, title_tally[i].title))
      special_title_list.append(combined_tuple)
      quicksort_tuple(special_title_list, 0, len(special_title_list) -1)

    for i in range(len(special_title_list)):

      print(f" {i+1}: {special_title_list[i][1][1]}")
      print(f"     - {sort_type}: {special_title_list[i][0]}")
      print(genre_string)



 # RECOMMENDATION PROGRAM

def get_recommended_list(hashmap, bfs_dfs = "dfs"):

  user_input = "r"

  while user_input != "q":

    # variables

    if user_input == "r":

      # clears all user_data for a complete restart
      user_data.wipe_user_data()

      recommended_length = None
      possible_sorting_inputs = (1,2,3,4,5,6,7,8,9,"m","q")
      possible_title_inputs = (1,2,3,4,5)
      input_modifier_match = (1,.5,.25,.5,1)
      input_like_hate_match = ("hate", "hate", "like", "like", "like")
      user_input = None
      tally_refresh = True
      title_tally = None
      title_to_node_played_games = []


      # accesses gr_userdata and runs through the questionaire to collect user preferences
      while len(list(user_data.all_user_likes.keys())) <= 0:
        
        get_user_data(None, "n", True, True)

        if len(list(user_data.all_user_likes.keys())) <= 0:

          print("\nYou need to have at least one liked genre or title to get a list of recommended games.")

          while user_input != "y":

            user_input = input("Do you want to try again.\n(y)es or (n)o:")

            if user_input == "n":

              return


      # ask user for number of titles they would like to be recommended
      while isinstance(recommended_length, int) == False:
        print("\nHow many games would you like to be recommended?\nList size depends on preferences and availability.")
        user_input = input("\n(Default is 5): ")
        try:
          recommended_length = int(user_input)

          if recommended_length <= 0:
            recommended_length = 5
        except:
          pass

  #while user_input != "q":

    while user_input not in ("y", "n"):

      new_user_likes_hates = {}

      if user_input != "m":

        # until I find a better way, played games used by the bfs search needs to be in node form.
        # this replaces strings with nodes
        if tally_refresh == True:

          title_to_node_played_games = user_data.played_games + []
          for i in range(len(title_to_node_played_games)):
            current_title_string = title_to_node_played_games[i]
            current_title_node = game_nodes.get_value(current_title_string)
            title_to_node_played_games[i] = current_title_node


          if bfs_dfs == "bfs":
          # bfs returns a dictionary with {title: [total_percentage, total times searched]
          # the games that the player would like should be the most accessed with the highest like percentage through the search algorithm.
            title_tally = bfs(hashmap, user_data.some_user_likes, user_data.some_user_hates, title_to_node_played_games)
            title_tally = average_tally(title_tally, recommended_length)

            clear_screen()

            print(f"\nHere are {len(title_tally)} games that you might like to try:\n")

            print_recommend_list_genre(title_tally, bfs_dfs)
            print()

          else:
          # dfs returns a list of titles (nodes)
          # no need for percentages, just the names of the games - the percentage comparison happens in the search
            title_tally = dfs(hashmap, user_data.some_user_likes, user_data.unique_game, title_to_node_played_games, 30, recommended_length)

            clear_screen()

            print(f"\nHere are {len(title_tally)} games that you might like to try:\n")

            print_recommend_list_genre(title_tally, bfs_dfs)
            print()

          # debug - print(f"title_tally - {title_tally}")

          tally_refresh = False

      else:

        clear_screen()

        print_recommend_list_genre(title_tally, bfs_dfs)
        print()



      print("Are there any games in the list you like or hate?\n(choose \"no\" if you would like to keep this list anyways)\n")
      user_input = input("(y)es or (n)o: ")

      # allows the user to choose and like\hate a recommended game they've already played, so it will be added to their preferences
      # and removed from possible recommended games.
      if user_input == "y":
        while user_input != "d":

          clear_screen()

          print_recommend_list_genre(title_tally, bfs_dfs)
          print()
          user_input = input("Enter the number next to the game you've played. Enter (d) if you're done: ")

          # debug - print(f"title_tally - {title_tally[user_input - 1].title}")

          if user_input != "d":
            try:
              user_input = int(user_input)
              if bfs_dfs == "bfs":
                temp_title = title_tally[user_input - 1][1].title
              else:
                temp_title = title_tally[user_input -1].title

                # debug - print(f"title_tally ---> {title_tally}")

            except:
              user_input = -1
          
            if user_input > 0 and user_input <= len(title_tally):

              print(f"\n{temp_title}:\n\n (5) Loved it!\n (4) Liked it.\n (3) Neutral.\n (2) Rather play something else.\n (1) Absolutely hated it!\n\n (c)ancel\n")

              user_input = input(f"\nEnter the number for your preference or enter \"c\" to cancel.")              

              try:
                user_input = int(user_input)
                new_user_likes_hates[temp_title] = [input_like_hate_match[user_input - 1], input_modifier_match[user_input - 1]]
              except:
                user_input = -1

              # debug - print(f"\nnew_user_likes_hates - {new_user_likes_hates}")       


        get_user_data(new_user_likes_hates, "n", False, False)
        tally_refresh = True


    user_input = None


    # The final list has been chosen and can be resorted using some extra sorting options.
    # "m" allows the user to go back, "q" allows the user to quit
    while user_input not in ("m", "r", "q"):

      clear_screen()

      print("\nRight now your recommended games are listed by relevance to your genre preferences.\n")
      
      # debug - print(f"user_input --- {user_input}")

      if user_input == None:
        print_recommend_list_genre(title_tally, bfs_dfs)
        print()
      else:
        print_recommend_list_special(title_tally, list(special_sample.keys())[user_input - 1], bfs_dfs)
        print()

      print("\nYou can also sort the list by:\n")

      for i in range(len(list(special_sample.keys()))):
        print(f" {i+1}: {list(special_sample.keys())[i]}")
  
      print("\nChoose the number next to the sorting method, or...\n(m) for more preference questions\n(r) for a complete refresh\n(q) to quit")
      user_input = input("> ")

      try:
        user_input = int(user_input)
        if user_input < 1 or user_input > len(list(special_sample.keys())):
          user_input = None
    
      except:
        if user_input not in ("m", "r", "q"):
          user_input = None
        
        
      if user_input == "m":
        tally_refresh = True





# STARTS RECOMMENDATION PROGRAM

get_recommended_list(game_averages, "dfs")















