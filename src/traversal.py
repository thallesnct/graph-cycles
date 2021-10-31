from .helpers.factories import generate_adjancency_list
from .helpers.immutable import (copy_path_and_add_vertex, copy_path_and_add_edge_path)
from .helpers.validators import validate_and_add_to_lists

def dfs(vertex, adjancency_list, visited, all_cycles, all_edge_cycles, path = [], edge_path = set()):
  if (visited.get(vertex) is True):
    if (len(path) > 0 and vertex is path[0] and len(path) > 2):
      validate_and_add_to_lists(vertex, path, edge_path, all_cycles, all_edge_cycles)
    return

  visited[vertex] = True
  new_path = copy_path_and_add_vertex(vertex, path)
  new_edge_path = edge_path

  if len(new_path) > 1:
    new_edge_path = copy_path_and_add_edge_path(path[len(path)-1], vertex, edge_path)

  for child in adjancency_list[vertex]:
    new_visited = visited.copy()
    dfs(child, adjancency_list, new_visited, all_cycles, all_edge_cycles, new_path, new_edge_path)

def find_cycles_by_traversal(graph):
  adjancency_list = generate_adjancency_list(graph)

  all_cycles = list()
  all_edge_cycles = list()

  for vertex in graph['vertices']:
    visited = dict()

    dfs(vertex, adjancency_list, visited, all_cycles, all_edge_cycles)

  return all_cycles  