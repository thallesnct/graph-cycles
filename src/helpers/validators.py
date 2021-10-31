from .contains_in_cycle import cycle_list_contains_path, cycle_list_contains_edge_path
from .immutable import copy_path_and_add_vertex, copy_path_and_add_edge_path

def validate_and_add_to_lists(vertex, path, edge_path, all_cycles, all_edge_cycles):
  new_path = copy_path_and_add_vertex(vertex, path)
  new_edge_path = copy_path_and_add_edge_path(path[len(path)-1], vertex, edge_path)

  if not cycle_list_contains_edge_path(new_edge_path, all_edge_cycles) and not cycle_list_contains_path(new_path, all_cycles):
    all_cycles.append(new_path)
    all_edge_cycles.append(new_edge_path)