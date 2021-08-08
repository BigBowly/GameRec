from gr_genregraph import GenreGraph
from gr_graphhashmap import GraphHashmap
from gr_node import GameNode
from gr_hashmap import Hashmap
from game_database_sep import genre_sample, special_sample, genre_dict, special_dict, game_nodes
from gr_creategraphs import create_graph_lists, check_graph_length
from random import randrange, choices, shuffle
from gr_maxheap import maxheaper
from gr_miscfunctions import clear_screen


# variables

# It helped to create a user_data class with common variables to avoid as many function arguments
class UserData:
  def __init__(self):
    self.all_user_likes = {}
    self.all_user_hates = {}
    self.some_user_likes = {}
    self.some_user_hates = {}
    self.played_games = []
    self.unique_game = ""

  def wipe_user_data(self):
    self.all_user_likes = {}
    self.all_user_hates = {}
    self.some_user_likes = {}
    self.some_user_hates = {}
    self.played_games = []
    self.unique_game = ""



# removes na (Not Applicable) from the final genre or game dict, leaving only the likes and hates
def remove_na(temp_dict):

  new_dict = {}

  for key, value in temp_dict.items():
    if value[0] != "NA":
      new_dict[key] = value

  return new_dict


# I like using random ranges more than choices - more reliable
# creates the random game list for the title and genre questions
def get_idx_list(key_list):

  idx_list = []

  while len(idx_list) < 10:
    idx = randrange(0, len(key_list))
    if idx not in idx_list:
      idx_list.append(idx)

  return idx_list



# QUESTIONS START

def start_question(again = False):

  clear_screen()

  user_input = None

  if again == False:

    print("To get recommendations, we need to establish what kind of games you like to play.")

  print("Would you like to describe your tastes using genres or titles?")

  while user_input not in ("g", "t"):
  
    user_input = input("(g)enres or (t)itles: ")

  if user_input == "t":
    return "titles"
  else:
    return "genres"


# allows the user to choose one unique game they like to be used as the 'end target' in the dfs search I'll eventually make.
def unique_game_question(list_size = 5):

  unique_game_title = None
  # possible_inputs = ("r",1,2,3,4,5)
  refresh = True
  title_keys = list(genre_dict.keys())

  while refresh == True:
    refresh = False
    idx_list = []
    temp_game_list = []
    user_input = -1

    if list_size > len(title_keys):
      for i in range(len(title_keys)):
        idx_list.append(i)
      shuffle(idx_list)

    else:
    #  while len(idx_list) < list_size:
    #    idx = randrange(0, len(list(genre_dict.keys())))
    #    if idx not in idx_list:
    #      idx_list.append(idx)

      idx_list = get_idx_list(title_keys)

    print("\nHere is a random list of games:\n")

    for i in range(len(idx_list)):
      rand_title = game_nodes.get_value(title_keys[idx_list[i]])
      temp_game_list.append(rand_title)
      if i < 9:
        print(f"  {i+1}: {rand_title.title}")
      else:
        print(f" {i+1}: {rand_title.title}")

    user_input = -1

    while user_input < 1 or user_input > len(idx_list):
      
      user_input = input("\nEnter the number next to your favorite title.\nIf you aren't happy with any of them, use (r) to refresh the list: ")

      if user_input == "r":
        refresh = True
        user_input = 1

      else:

        try:
          user_input = int(user_input)
        except:
          print("Not an acceptable response.")
          user_input = 0

  # unique game is a GameNode
  user_data.unique_game = temp_game_list[user_input - 1]
  user_data.played_games.append(user_data.unique_game.title)
  
  # debug - print(f"user_data - {user_data.unique_game}")  


# likes and hates question based on genre - user rates 0-5 (hate-like) how they feel about a genre
# this will be passed into the averaging function in gr_userdata to help define all_user_likes and all_user_hates
def like_hate_genre_question():
  
  genre_rating_dict = {}
  idx_list = []
  genre_keys = list(genre_sample.keys())
  genre_liked = False

  # matching lists to possible inputs
  possible_inputs = (0,1,2,3,4,5)
  input_percentage_match = ("NA", 1, .5, .25, .5, 1)
  input_like_hate_match = ("NA", "hate", "hate", "like", "like", "like")

  # get random index list
  idx_list = get_idx_list(genre_keys)

  print("\nWe're going to run through 10 random genres. Answer with...\n")
  print(" (5) Love it\n (4) Like it\n (3) Neutral\n (2) Not really\n (1) Absolutely hate it\n\n (0) Unsure\n")

  while len(list(genre_rating_dict.keys())) < 10:
    user_input = -1
    current_idx = idx_list.pop()
    while user_input not in possible_inputs:
      genre_print = (f"{genre_keys[current_idx]}: ")
      user_input = int(input(genre_print.upper()))

      try:
        user_input = int(user_input)
      except:
        user_input = -1
    
    # creation of the user likes dictionary requires at least one like.
    if input_like_hate_match[user_input] == "like":
      genre_liked = True

    genre_rating_dict[genre_keys[current_idx]] = (input_like_hate_match[user_input], input_percentage_match[user_input])


  # if user likes was created previously from a different question, this will allow the user to move on
  if genre_liked == True or len(list(user_data.all_user_likes.keys())) > 0:
    genre_rating_dict = remove_na(genre_rating_dict)


    # returns dictionary - {genre: (like\hate, modifier), genre: (like\hate, modifier), . . .}
    return genre_rating_dict

  else:
    print("\nTo give recommendations, there needs to be at least one neutral, liked, or loved genre.")

    while user_input not in ("y", "n", "g"):
      user_input = input("Try again or define your likes from a list of games? (y)es, (n)o, or (g)ames:")

    if user_input == "y":
      return 0

    if user_input == "g":
      return 1
    
  return None


# likes and hates question based on game - user rates 0-5 (hate-like) how they feel about specific games
# the game will be passed into the averaging function in gr_userdata
# their genre edges will be averaged to help define all_user_likes and all_user_hates
def like_hate_game_question():

  game_rating_dict = {}
  idx_list = []
  game_keys = list(genre_dict.keys())
  game_liked = False

  # matching lists to possible inputs
  possible_inputs = (0,1,2,3,4,5,6)
  input_percentage_match = ("NA",.25, 1, .5, .25, .5, 1)
  input_like_hate_match = ("NA", "interested", "hate", "hate", "like", "like", "like")

  idx_list = get_idx_list(game_keys)

  print("\nWe're going to run through 10 random games. Answer with...\n")
  print(" (6) Loved it\n (5) Liked it\n (4) Neutral\n (3) Rather play something else\n (2) Absolutely hated it\n\n (1) Never played, but interested\n (0) Never played, not interested\n")

  while len(list(game_rating_dict.keys())) < 10:
    user_input = -1
    current_idx = idx_list.pop()
    while user_input not in possible_inputs:
      game_print = (f"{game_keys[current_idx]}: ")
      user_input = input(game_print)

      try:
        user_input = int(user_input)
      except:
        user_input = -1

    if input_like_hate_match[user_input] == "like" or input_like_hate_match[user_input] == "interested":
      game_liked = True

    game_rating_dict[game_keys[current_idx]] = (input_like_hate_match[user_input], input_percentage_match[user_input])


  # checks to make sure there's enough information to create user preferences(user_likes)
  # the algorithms require some likes
  if game_liked == True or len(list(user_data.all_user_likes.keys())) > 0:
    game_rating_dict = remove_na(game_rating_dict)


    # returns this - {title: (like\hate, modifier), title: (like\hate, modifier), . . .}
    # the title is a string, not the actual node
    return game_rating_dict

  else:
    print("\nTo give recommendations, there needs to be at least one neutral, liked, or loved game.")
   
    while user_input not in ("y", "n", "g"):
      user_input = input("Try again or define your likes from a list of genres? (y)es, (n)o, or (g)enres:")

    if user_input == "y":
      return 1

    if user_input == "g":
      return 0
    
  return None




# CALCULATE USER PREFS START


# f(x) = y1 + ((y2 - y1)/(x2 - x1))(x - x1)
def adjust_curve(current_value, max_old_value, min_old_value, max_new_value, min_new_value):

  if current_value == 0:
    return 0

  adj_value = int(max_new_value + ((min_new_value - max_new_value)/(min_old_value - max_old_value)) * (current_value - max_old_value))
  return adj_value


# gets a single list based on the genre and averages out all the other genre tags in the titles that populate that genre graph
# this is meant to build a user_likes key list based on genres commonly associated with the main genre
def find_genre_averages(hashmap, key_list, genre, modifier):
  single_title_list = hashmap.get_single_graph(genre).create_list(True, 10)

  # debug - print(f"{genre} - single_title_list - {single_title_list}")

  genres_total_dict = {}
  averages_list = []
  title_count = len(single_title_list)

  for title in single_title_list:
    title_genre_percent = title[1].genre_edges.get_value(genre)
    percent_shift_value = 0
    for value, genre_tag in title[1].genre_edges.get_item_list(False):
      
      # modifier adjusts the final percent - the modifier is based on how much the genre is liked or hated
      if title_genre_percent <= 0:
        percent_shift_value = 0 * value
      else:
        percent_shift_value = modifier * ((title_genre_percent/100) * value)

      # adjusts old percentage or adds new percentage to dictionary
      if genre_tag in genres_total_dict.keys():
        genres_total_genre_value = genres_total_dict[genre_tag]
        genres_total_dict[genre_tag] = genres_total_genre_value + percent_shift_value
      else:
        genres_total_dict[genre_tag] = percent_shift_value

  # found a max heap works better than a tuple quicksort for some reason
  for genre_tag in genres_total_dict:
    if genres_total_dict[genre_tag] == 0:
      maxheaper.push(averages_list, [0, genre_tag])
    else:      
      maxheaper.push(averages_list, [int(genres_total_dict[genre_tag]/title_count), genre_tag])

  averages_list = maxheaper.sort(averages_list)

  # adjusting for the curve - not completely necessary, but threshholds in other parts of the code work within the bounds
  # of 0 - 100 percent. This will raise the user_likes upper levels to keep graph lists from being empty.
  if len(averages_list) <= 0:
    print(f"The genre graph {genre} doesn't have any games to average.")
  else:
    
    max_value = averages_list[0][0]
    min_value = averages_list[-1][0]    
    for item in averages_list:
      
      current_value = item[0]
      adjusted_value = adjust_curve(current_value, max_value, min_value, 100, 0)
      item[0] = adjusted_value
      


  #return [genre, averages_list]

  # returns this - [(percentage, genre), (percentage, genre), . . .]
  return averages_list



# like find_genre_averages, but for the titles question
# except the averages for titles are formed create_all_user_dicts function
# this takes those final results and curves them - adjusts the largest value to 100 and adjusts the rest by that percentage. 
def find_title_curves(user_prefs):
  prefs = []

  for key, value in user_prefs.items():
    maxheaper.push(prefs, [value, key])
    prefs = maxheaper.sort(prefs)

  # adjusting for the curve - not completely necessary, but threshholds in other parts of the code work within the bounds
  # of 0 - 100 percent. This will raise the user_likes upper levels to keep graph lists from being empty.

  if len(prefs) <= 0:
    pass

  else:
    max_value = prefs[0][0]
    min_value = prefs[-1][0]

    for item in prefs:
      current_value = item[0]
      adjusted_value = adjust_curve(current_value, max_value, min_value, 100, 0)
      item[0] = adjusted_value
      user_prefs[item[1]] = item[0]

  # debug - print(f"prefs -- {prefs}\n")



# After the user gets a recommended list, they can choose which of the titles they've played before and whether they liked or 
# hated the games. We can then enter those new titles genre percentages into the user likes dictionaries here
def refresh_title_user_dicts(new_prefs, user_likes, user_hates, played_games):
  temp_user_likes = {}
  temp_user_hates = {}
  like_count = 0
  hate_count = 0
    
  if len(new_prefs) <= 0:
    return

  for title in new_prefs:
    if title not in played_games:
      played_games.append(title)

    if new_prefs[title][0] == "like":
      like_count += 1

      # debug - print(f"refresh - user_likes - {user_likes}")
      # debug - print(f"refresh - temp_user_likes - {temp_user_likes}")
      # debug - print(f"refresh - user_likes - {list(user_likes.keys())}")
      # debug - print(f"refresh - temp_user_likes - {len(list(temp_user_likes.keys()))}")

      for value, key in game_nodes.get_value(title).genre_edges.get_item_list():
        if key not in list(temp_user_likes.keys()):
          temp_user_likes[key] = int(new_prefs[title][1] * value)
        else:
          old_value = temp_user_likes[key]
          temp_user_likes[key] = int(old_value + (new_prefs[title][1] * value))

    if new_prefs[title][0] == "hate":
      hate_count += 1

      for value, key in game_nodes.get_value(title).genre_edges.get_item_list():
        if key not in list(temp_user_hates.keys()):
          temp_user_hates[key] = int(new_prefs[title][1] * value)
        else:
          old_value = temp_user_hates[key]
          temp_user_hates[key] = int(old_value + (new_prefs[title][1] * value))


  # averages the new likes and hates, re-adjusts for the curve, and then correctly averages the new values with the old values
  if like_count > 0:
    for genre in temp_user_likes:
      new_value = temp_user_likes[genre]/like_count
      temp_user_likes[genre] = new_value

    find_title_curves(temp_user_likes)

    if len(list(user_likes.keys())) > 0:
      for key, value in temp_user_likes.items():
        new_average = int((value + user_likes[key]) / 2)
        user_likes[key] = new_average
    else:
      for key, value in temp_user_likes.items():
        user_likes[key] = value


  if hate_count > 0:
    for genre in temp_user_hates:
      new_value = temp_user_hates[genre]/hate_count
      temp_user_hates[genre] = new_value
  
    find_title_curves(temp_user_hates)

    if len(list(user_hates.keys())) > 0:
      for key, value in temp_user_hates.items():
        new_average = int((value + user_hates[key]) / 2)
        user_hates[key] = new_average
    else:
      for key, value in temp_user_hates.items():
        user_hates[key] = value



# main user_data function that asks the genre and title questions. The resulting genre dictionaries are then averaged and graded on
# a curve and returned to the all_user_likes/hates dictionaries used by gr_main.py
# it can be used more than once - the new values will be averaged with the old all_user_likes/hates dictionaries
def create_all_user_dicts(hashmap, question_type, user_likes, user_hates, played_games):

  switch = True
  question_tuple = ("genres", "titles")
  temp_user_likes = {}
  temp_user_hates = {}
  like_count = 0
  hate_count = 0
  

  # asks the question - user chooses genre or titles to decide preferences
  # switch value allows switching in case the user can't get an adequate result from either
  while switch == True:
    if question_type == "genres":
      switch = False
      question_dict = like_hate_genre_question()

      if question_dict == None:
          return

      if isinstance(question_dict, dict) == False:
        question_type = question_tuple[question_dict]
        switch = True
    elif question_type == "titles":
      switch = False
      question_dict = like_hate_game_question()

      if question_dict == None:
          return

      if isinstance(question_dict, dict) == False:
        question_type = question_tuple[question_dict]
        switch = True
    else:
      return


  # total of all genre likes and hates from the questionaire
  if question_type == "genres":
    like_count = 0
    hate_count = 0
    for genre in question_dict:
      if question_dict[genre][0] == "like":
        like_count += 1
        single_genre_average = (find_genre_averages(hashmap, genre_sample, genre, question_dict[genre][1]))

        # debug - print(f"single_genre_average - like - {single_genre_average}")

        if len(list(temp_user_likes.keys())) != 0:
          for sga in single_genre_average:
            current_value = sga[0]
            total_value = int(temp_user_likes[sga[1]] + current_value)
            temp_user_likes[sga[1]] = total_value

        else:
          for sga in single_genre_average:
            current_value = sga[0]
            temp_user_likes[sga[1]] = current_value

      elif question_dict[genre][0] == "hate":
        hate_count += 1
        single_genre_average = (find_genre_averages(hashmap, genre_sample, genre, question_dict[genre][1]))

        # debug - print(f"single_genre_average - hate - {single_genre_average}")

        if len(list(temp_user_hates.keys())) != 0:
          for sga in single_genre_average:
            current_value = sga[0]
            total_value = int(temp_user_hates[sga[1]] + current_value)
            temp_user_hates[sga[1]] = total_value

        else:
          for sga in single_genre_average:
            current_value = sga[0]
            temp_user_hates[sga[1]] = current_value

    # return genre_like_averages, genre_hate_averages
    for key, value in temp_user_likes.items():
      if value != 0:
        temp_user_likes[key] = int(value/like_count)

    for key, value in temp_user_hates.items():
      if value != 0:
        temp_user_hates[key] = int(value/hate_count)




  # total of all title likes and hates from the questionaire
  # averages the genre_edges of each title
  elif question_type == "titles":
    like_count = 0
    hate_count = 0
    for title in question_dict:

      # unique addition to the titles section - adds rated titles to the played games list
      # this list eventually makes it to the graphsearch where it removes already played games from the recommended list.
      if question_dict[title][0] != "interested" or title in played_games:
        played_games.append(title)

      # debug - print(f"played_games - {played_games}")
      
      if question_dict[title][0] == "like" or question_dict[title][0] == "interested":
        like_count += 1

        # debug - print(f"modifier - {title} -  {question_dict[title][1]}")
        
        title_genre_item_list = game_nodes.get_value(title).genre_edges.get_item_list()

        if len(list(temp_user_likes.keys())) != 0:
          for value, key in title_genre_item_list:
            current_value = value
            total_value = int(temp_user_likes[key] + (question_dict[title][1] * current_value))
            temp_user_likes[key] = total_value

        else:
          for value, key in title_genre_item_list:
            current_value = value
            temp_user_likes[key] = int(question_dict[title][1] * current_value)

      elif question_dict[title][0] == "hate":
        hate_count += 1
        
        title_genre_item_list = game_nodes.get_value(title).genre_edges.get_item_list()

        if len(list(temp_user_hates.keys())) != 0:
          for value, key in title_genre_item_list:
            current_value = value
            total_value = int(temp_user_hates[key] + (question_dict[title][1] * current_value))
            temp_user_hates[key] = total_value

        else:
          for value, key in title_genre_item_list:
            current_value = value
            temp_user_hates[key] = int(question_dict[title][1] * current_value)

    for key, value in temp_user_likes.items():
      if value != 0:
        temp_user_likes[key] = int(value/like_count)

    for key, value in temp_user_hates.items():
      if value != 0:
        temp_user_hates[key] = int(value/hate_count)


    find_title_curves(temp_user_likes)
    find_title_curves(temp_user_hates)

  # in case the user_likes and user_hates aren't empty and this function is supplementing them
  # this correctly averages the new with the old 
  if len(list(user_likes.keys())) > 0:
    for key, value in temp_user_likes.items():
      new_average = int((value + user_likes[key]) / 2)
      user_likes[key] = new_average
  else:
    for key, value in temp_user_likes.items():
      user_likes[key] = value

  if len(list(user_hates.keys())) > 0:
    for key, value in temp_user_hates.items():
      new_average = int((value + user_hates[key]) / 2)
      user_hates[key] = new_average
  else:
    for key, value in temp_user_hates.items():
      user_hates[key] = value


  find_title_curves(user_likes)
  find_title_curves(user_hates)



# limits the user likes - if there are more than two genres with the same like percentage, it will randomly choose up to two
# uses a maxheap to grab the top values within a predefined threshhold
def sort_user_prefs(pref_dict, threshhold):

  temp_list = []
  new_dict = {}

  for key, value in pref_dict.items():

    # debug - print(f"(value,key) - ({value}, {key})")

    maxheaper.push(temp_list, (value,key))

  sorted_temp_list = maxheaper.sort_threshhold(temp_list, threshhold)

  for item in sorted_temp_list:
    if len(item) > 2:
      temp = choices(item, k=2)
      for rand_genre in temp:
        new_dict[rand_genre[1]] = rand_genre[0]

    else:
      for rand_genre in item:
        new_dict[rand_genre[1]] = rand_genre[0]

  # debug - print(sorted_temp_list)

  # debug - for item in sorted_temp_list:
  #  debug - new_dict[item[1]] = item[0]

  return new_dict


# since the some_user dictionaries are randomly chosen in some cases, this will allow a refresh if needed or wanted
def refresh_sort(prefs, threshhold):
  if prefs == "likes":
    some_user_likes = sort_user_prefs(all_user_likes, threshhold)
  elif prefs == "hates":
    some_user_hates = sort_user_prefs(all_user_hates, threshhold)

  return


# takes the all_likes dictionaries and creates truncated versions - just in case a huge amount of tags causes
# the graph search to slow down.
# you can enter a threshhold to allow only genre percentages above a certain value
def create_some_dicts(all_dict, starting_threshhold):
  some_user_dict = {}
  threshhold = starting_threshhold

  # debug - print(f"length - {len(list(some_user_dict.keys()))}")

  while len(list(some_user_dict.keys())) <= 0 and threshhold > -10:

    some_user_dict = sort_user_prefs(all_dict, threshhold)

    # debug - print(f"sud - {some_user_dict}")

    threshhold -= 10

  return some_user_dict




# USER DATA HUB

def get_user_data(like_hate_additions = None, continue_questions = "n", refresh = True, pick_another_title = True):

  # for first time use and in case new information were to appear and a refresh of the list was needed
  if refresh == True:

    # user_data.wipe_user_data()
    continue_questions = "y"
    pick_another_title = True
    refresh = False

  # allows for continued averaging to hopefully fine-tune the user_likes for more accurate recommendations
  while continue_questions == "y":
    continue_questions = "r"
    question_type = start_question(True)
    create_all_user_dicts(game_averages, question_type, user_data.all_user_likes, user_data.all_user_hates, user_data.played_games)

    print("\nYou can answer the questions again to try to fine-tune your preferences. Would you like to?")

    while continue_questions not in ("y", "n"):

      continue_questions = input("(y)es or (n)o? ")


  # after the recommendations have been made, the user can select which of those games they like or hate - meaning
  # they've played them already, and can be averaged and added to the played_games list so they don't end up being
  # recommended again.

  if len(list(user_data.all_user_likes.keys())) <= 0:

    return

  if like_hate_additions != None:
    refresh_title_user_dicts(like_hate_additions, user_data.all_user_likes, user_data.all_user_hates, user_data.played_games)

  # debug - print(f"\nall_user_likes - {user_data.all_user_likes}")
  # debug - print(f"\nall_user_hates - {user_data.all_user_hates}")

  user_data.some_user_likes = create_some_dicts(user_data.all_user_likes, 50)
  user_data.some_user_hates = create_some_dicts(user_data.all_user_hates, 50)

  # debug - print(f"\nsul - {user_data.some_user_likes}")
  # debug - print(f"\nsuh - {user_data.some_user_hates}")
  # debug - print(f"\nplayed_games --- {user_data.played_games}")

  if pick_another_title == True:

    pick_another_title = False
    unique_game_question(10)

  
    
# CREATE GAME HASHMAP

# create genre graph hashmap
game_averages = GraphHashmap("Game Averages")
# create empty graphs within the hashmap
game_averages.create_graphs(genre_sample)
# fill the graph lists with game nodes
create_graph_lists(game_averages, genre_sample, None, 70)
# checks graph lengths and will adjust the threshhold of the graphs that don't contain enough games
check_graph_length(game_averages, genre_sample)
# creates the user_data class to store variables without having to use a bunch of arguments
user_data = UserData()

