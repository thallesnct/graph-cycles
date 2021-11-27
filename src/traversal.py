from .helpers.factories import generate_adjacency_list
from .helpers.immutable import (copy_path_and_add_vertex, copy_path_and_add_edge_path)
from .helpers.validators import validate_and_add_to_lists

def dfs(vertex, adjacency_list, visited, all_cycles, all_edge_cycles, path = [], edge_path = set()):
  if (visited.get(vertex) is True):
    if (len(path) > 2 and vertex is path[0]):
      validate_and_add_to_lists(vertex, path, edge_path, all_cycles, all_edge_cycles)
    return

  new_visited = visited.copy()
  new_visited[vertex] = True
  new_path = copy_path_and_add_vertex(vertex, path)
  new_edge_path = edge_path

  if len(new_path) > 1:
    new_edge_path = copy_path_and_add_edge_path(path[len(path)-1], vertex, edge_path)

  for child in adjacency_list[vertex]:
    dfs(child, adjacency_list, new_visited, all_cycles, all_edge_cycles, new_path, new_edge_path)

# O(n+m)
# n = number of vertices
# m = number of edges
def find_cycles_by_traversal(graph):
  adjacency_list = generate_adjacency_list(graph)

  all_cycles = list()
  all_edge_cycles = list()

  for vertex in graph['vertices']:
    visited = dict()

    dfs(vertex, adjacency_list, visited, all_cycles, all_edge_cycles)

  return all_cycles  