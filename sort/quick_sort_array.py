array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort_array(array):
  if len(array) <= 1:
    return array

  pivot = array[0]
  tail = array[1:]

  left_side = [x for x in tail if x <= pivot]
  right_side = [x for x in tail if x > pivot]

  return quick_sort_array(left_side) + [pivot]+ quick_sort_array(right_side)

print(quick_sort_array(array))
