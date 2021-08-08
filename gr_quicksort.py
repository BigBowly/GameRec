from random import randrange
from game_database_sep import genre_dict, special_dict, genre_sample, special_sample


# quicksort for sorting game_lists by whatever metric the sample dicitonaries have
def quicksort(game_list, start_idx, end_idx, sort_value):
  
  if start_idx >= end_idx:
    return

  rand_idx = randrange(start_idx, end_idx + 1)
  rand_value = game_list[rand_idx].genre_edges.get_value(sort_value)

  game_list[rand_idx], game_list[end_idx] = game_list[end_idx], game_list[rand_idx]
  current_idx = start_idx
  mid_idx = start_idx
  
  while current_idx != end_idx:
    current_value = game_list[current_idx].genre_edges.get_value(sort_value)

    if current_value >= rand_value:
      game_list[current_idx], game_list[mid_idx] = game_list[mid_idx], game_list[current_idx]
      current_idx += 1
      mid_idx += 1
    else:
      current_idx += 1

  game_list[mid_idx], game_list[end_idx] = game_list[end_idx], game_list[mid_idx]

  quicksort(game_list, 0, mid_idx-1, sort_value)
  quicksort(game_list, mid_idx+1, end_idx, sort_value)

  return


# quicksort specifically for tuples
def quicksort_tuple(tuple_list, start_idx, end_idx):
  
  if start_idx >= end_idx:
    return

  rand_idx = randrange(start_idx, end_idx + 1)
  rand_value = tuple_list[rand_idx][0]

  tuple_list[rand_idx], tuple_list[end_idx] = tuple_list[end_idx], tuple_list[rand_idx]
  current_idx = start_idx
  mid_idx = start_idx
  
  while current_idx != end_idx:
    current_value = tuple_list[current_idx][0]

    if current_value >= rand_value:
      tuple_list[current_idx], tuple_list[mid_idx] = tuple_list[mid_idx], tuple_list[current_idx]
      current_idx += 1
      mid_idx += 1
    else:
      current_idx += 1

  tuple_list[mid_idx], tuple_list[end_idx] = tuple_list[end_idx], tuple_list[mid_idx]

  quicksort_tuple(tuple_list, 0, mid_idx-1)
  quicksort_tuple(tuple_list, mid_idx+1, end_idx)

  return




# DEBUG CODE

## test = [5,2,10,7,20,6,8,3]
#test = [(5, "blah"),(2, "blah"),(10, "blah"),(7, "blah"),(20, "blah"),(6, "blah"),(8, "blah"),(3, "blah")]

## quicksort(test, 0, len(test) - 1, 0)
#quicksort_tuple(test, 0, len(test) - 1)

#print(test)
