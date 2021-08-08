from gr_hashmap import Hashmap
from gr_node import GameNode


class Maxheap:

  # count - defined by the size of the heap entered - used to find the last entry in the binary tree
  # type_match - class can take single values or list/tuple values in form (compared value, ???)
  #            - makes sure types match
  # is_tuple - are the values tuple/lists or single values

  # class doesn't make copies - changes the original heap passed through
 
  def __init__(self):
    # count is defined by the length of whatever heap the user chooses to use
    self.count = 0
    self.type_match = True
    self.is_tuple = False


  # functions that find the 3 parts of a tree when list[0] is None
  def find_parent_idx(self, idx):
    return int((idx - .5) // 2)

  def find_left_idx(self, idx):
    return idx * 2 + 1

  def find_right_idx(self, idx):
    return idx * 2 + 2


  # adds a value to the heap
  def push(self, heap, value):

    self.count = len(heap) - 1    

    # checks for tuples/lists. doesn't accept a mixture of tuple and single value
    if self.count >= 0:
      self.type_match, self.is_tuple = self.check_tuple(heap[0], value)
      
      # debug - if self.type_match == False:
        # debug - return "Types don't match, no mixing of tuples and non-tuples."
      
      heap.append(value)
      self.count += 1
      self.heapify_up(heap)

    else:
      heap.append(value)
      self.count += 1


  # removes the top/minimum value from the heap
  def pull(self, heap):

    self.count = len(heap) - 1

    if self.count == 0:
      min_val = heap.pop()
      self.count -= 1
      return min_val
    
    elif self.count > 0:
      heap[0], heap[self.count] = heap[self.count], heap[0]
      min_val = heap.pop()
      self.count -= 1

      self.heapify_down(heap)
      
      return min_val


  # reorders the heap when a value is added
  def heapify_up(self, heap):
    c_idx = self.count
    p_idx = self.find_parent_idx(c_idx)

    # finds the values - if the heap uses tuples/lists it will find variable[0]
    c_value, p_value = self.find_tuple_value_parent(heap, c_idx, p_idx)

    while c_value > p_value:
      heap[c_idx], heap[p_idx] = heap[p_idx], heap[c_idx]
      c_idx = p_idx
      p_idx = self.find_parent_idx(c_idx)

      if p_idx < 0:
        break

      c_value, p_value = self.find_tuple_value_parent(heap, c_idx, p_idx)

    return heap


  # reorders the heap when a value is removed
  def heapify_down(self, heap):
    c_idx = 0
    l_idx = self.find_left_idx(c_idx)
    r_idx = self.find_right_idx(c_idx)

    while l_idx <= self.count:

      # again finds variable[0] if using tuples/lists
      c_value, l_value = self.find_tuple_value_child(heap, c_idx, l_idx)

      if r_idx <= self.count:

        c_value, l_value, r_value = self.find_tuple_value_child(heap, c_idx, l_idx, r_idx)

        if r_value > l_value and r_value >= c_value:
          heap[r_idx], heap[c_idx] = heap[c_idx], heap[r_idx]
          c_idx = r_idx
        elif l_value >= c_value:
          heap[l_idx], heap[c_idx] = heap[c_idx], heap[l_idx]
          c_idx = l_idx
        else:
          c_idx = l_idx

      elif l_value >= c_value:
        heap[l_idx], heap[c_idx] = heap[c_idx], heap[l_idx]
        c_idx = l_idx
      else:
        c_idx = l_idx

      l_idx = self.find_left_idx(c_idx)
      r_idx = self.find_right_idx(c_idx)



  # takes a heap and returns a sorted heap - since its a min heap class it will return an ascending list
  def sort(self, heap):
    sorted_heap = []
    heap_copy = heap + []
    self.count = len(heap) - 1

    while self.count >= 0:
      max_value = self.pull(heap_copy)
      sorted_heap.append(max_value)

    return sorted_heap


  # like the sort function except it will stop pulling nodes once they are lower than the threshhold argument
  # sorting by a specific type of value is handled in whichever file calls this function in how it creates its tuples 
  def sort_threshhold(self, heap, threshhold):
    sorted_heap = []
    heap_copy = heap + []
    self.count = len(heap) - 1
    test_value = None
    previous_value = -1

    while self.count >= 0:
      max_value = self.pull(heap_copy)
      if isinstance(max_value, tuple) == True:
        self.is_tuple = True

      if self.is_tuple == True:
        test_value = max_value[0]
      else:
        test_value = max_value

      if test_value >= threshhold:
        if test_value == previous_value:
          sorted_heap[-1].append(max_value)
        else:
          sorted_heap.append([max_value])
          previous_value = test_value
      else:
        break

    return sorted_heap


  # the original sort_threshhold function creates a special format of embedded lists for shuffling based on similar values
  # this allows for a more general sorting used by the majority of functions
  def sort_threshhold_v2(self, heap, threshhold):
    sorted_heap = []
    heap_copy = heap + []
    self.count = len(heap) - 1
    test_value = None
    previous_value = -1

    while self.count >= 0:
      max_value = self.pull(heap_copy)
      if isinstance(max_value, tuple) == True:
        self.is_tuple = True

      if self.is_tuple == True:
        test_value = max_value[0]
      else:
        test_value = max_value

      if test_value >= threshhold:
        if test_value == previous_value:
          sorted_heap.append(max_value)
        else:
          sorted_heap.append(max_value)
          previous_value = test_value
      else:
        break

    return sorted_heap


  # finds the current and parent values of two heap indexs being compared
  # if its a single value heap, a single value will be returned
  # if its a tuple/list heap, the first value in the tuple will be returned (index 0)
  def find_tuple_value_parent(self, heap, c_idx, p_idx):
    if self.is_tuple:
      c_value = heap[c_idx][0]
      p_value = heap[p_idx][0]
      
    else:
      c_value = heap[c_idx]
      p_value = heap[p_idx]

    return c_value, p_value


  # same with parent finder - returns either a single value or index 0 of tuple/list
  def find_tuple_value_child(self, heap, c_idx, l_idx, r_idx=None):
    if self.is_tuple:
      c_value = heap[c_idx][0]
      l_value = heap[l_idx][0]
      if r_idx != None:
        r_value = heap[r_idx][0]
    else:
      c_value = heap[c_idx]
      l_value = heap[l_idx]
      if r_idx != None:
        r_value = heap[r_idx]

    if r_idx:
      return c_value, l_value, r_value
    else:
      return c_value, l_value


  # checks if the heap uses tuples/lists or single values - doesn't allow mixing
  def check_tuple(self, value1, value2):
    tuple1 = isinstance(value1,tuple) or isinstance(value1, list)
    tuple2 = isinstance(value2,tuple) or isinstance(value2, list)

    if tuple1 == True and tuple2 == True:
      return True, True
    elif tuple1 == False and tuple2 == False:
      return True, False
    else:
      return False, False



# file imported by other files - allows for direct heaping of lists, no need for returns except when sorting

maxheaper = Maxheap()



# DEBUG CODE

#my_heap = []

#heaper.push(my_heap, 101)
#print(my_heap)

#heaper.push(my_heap, 30)

#print(my_heap)

#heaper.push(my_heap, -1)
#heaper.push(my_heap, 245)
#heaper.push(my_heap, 30)
#heaper.push(my_heap, 67)

#print(my_heap)

#my_heap_sort = heaper.sort(my_heap)

#print(my_heap_sort)


#my_tuple_heap = []

#heaper.push(my_tuple_heap, (0,"A"))
#heaper.push(my_tuple_heap, (4,"B"))
#heaper.push(my_tuple_heap, (10,"C"))
#heaper.push(my_tuple_heap, (6,"D"))
#heaper.push(my_tuple_heap, (8,"E"))

#print(my_tuple_heap)

#my_sorted_tuple = heaper.sort(my_tuple_heap)

#print(my_sorted_tuple)

#my_list_heap = []

#heaper.push(my_list_heap, [0,"A"])
#heaper.push(my_list_heap, [4,"B"])
#heaper.push(my_list_heap, [10,"C"])
#heaper.push(my_list_heap, [6,"D"])
#heaper.push(my_list_heap, [8,"E"])

#print(my_list_heap)



