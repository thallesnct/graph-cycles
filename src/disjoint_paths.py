from .helpers.factories import generate_adjacency_list
from .helpers.validators import validate_and_add_to_path_lists

def bfs(start_vertex, target_vertex, adjacency_list, visited_edges, all_paths): 
  queue = []

  queue.append([start_vertex])

  while queue:
    path = queue.pop(0)

    node = path[-1]

    if node == target_vertex:
      validate_and_add_to_path_lists(path, visited_edges, all_paths)
    else:
      for adjacent_vertex in adjacency_list.get(node, []):
        if (adjacent_vertex in path):
          continue

        new_path = list(path)
        new_path.append(adjacent_vertex)
        queue.append(new_path)

# O(n+m)
# n = number of vertices
# m = number of edges
def find_disjoint_paths(graph, from_vertex, to_vertex):
  adjacency_list = generate_adjacency_list(graph, is_directed_graph = True)

  all_paths = list()
  visited_edges = set()

  bfs(from_vertex, to_vertex, adjacency_list, visited_edges, all_paths)

  return all_paths