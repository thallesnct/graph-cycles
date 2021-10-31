def cycle_list_contains_path(path, cycle_list):
  is_in_list = False

  for path_arr in cycle_list:
    if len(path_arr) != len(path):
      continue

    if sorted(path_arr) == sorted(path):
      is_in_list = True
  
  return is_in_list

def cycle_list_contains_edge_path(edge_path, cycle_list):
  is_in_list = False

  for edge_set in cycle_list:
    if len(edge_set) != len(edge_path):
      continue

    set_diff = edge_set.difference(edge_path)

    if len(set_diff) == 0:
      is_in_list = True

  return is_in_list