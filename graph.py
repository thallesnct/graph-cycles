# Grafo exemplo
# graph = {
#   'vertices': [1, 2, 3, 4, 5],
#   'edges': ((1,3), (3,2), (4,5), (5,1), (2,4))
# }
import datetime

def calculate_adjancency_list(graph):
  adjancency_list = { vertex: set() for vertex in graph['vertices'] }

  for (vertex_a, vertex_b) in graph['edges']:
    adjancency_list[vertex_a].add(vertex_b)
    adjancency_list[vertex_b].add(vertex_a)

  return adjancency_list

def copy_path_and_add_vertex(vertex, path):
  new_path = path.copy()
  new_path.append(vertex)

  return new_path

def dfs(vertex, adjancency_list, visited, all_cycles, path = []):
  if (visited.get(vertex) is True):
    if (len(path) > 0 and vertex is path[0] and len(path) > 2):
      all_cycles.append(copy_path_and_add_vertex(vertex, path))
    return

  visited[vertex] = True
  new_path = copy_path_and_add_vertex(vertex, path)

  for child in adjancency_list[vertex]:
    new_visited = visited.copy()
    dfs(child, adjancency_list, new_visited, all_cycles, new_path)

def find_cycles_by_traversal(graph):
  adjancency_list = calculate_adjancency_list(graph)

  all_cycles = list()

  for vertex in graph['vertices']:
    visited = dict()

    dfs(vertex, adjancency_list, visited, all_cycles)

  return all_cycles  

def main():
  # graph = {
  #   'vertices': [1, 2, 3, 4, 5],
  #   'edges': ((1,3), (3,2), (4,5), (5,1), (2,4))
  # }
  # graph = {
  #   'vertices': list(range(1, 17)),
  #   'edges': ((1,2), (1,11), (1, 15), (2,11), (2,10), (2,3), (3,10), (3,4), (4,5), (5,6), (6,7), (7,8), (8,9), (8,14), (9, 10), (9,13), (11,12), (12, 13), (13,15), (14,16), (15,16))
  # }
  # graph = { 
  #   'vertices': list(range(1,9)),
  #   'edges': ((1,2), (2,3), (2,5), (3,4), (4,5), (5,6), (6,7), (6,8), (7,8))
  # }
  graph = { 
    'vertices': list(range(1, 7)),
    'edges': ((1,4), (1,2), (1,5), (2,3), (2,4), (2,5), (3,4), (3,5), (3,6), (4,6), (5,6))
  }


  start_time = datetime.datetime.now()

  cycles = find_cycles_by_traversal(graph)

  end_time = datetime.datetime.now()

  time_diff = (end_time - start_time)

  execution_time = time_diff.total_seconds() * 1000

  # Todo: Remove duplicate cycles
  print(cycles)
  print(f'took {execution_time}ms to run find_all_cycles_by_traversal')

if __name__ == "__main__":
   # Runs main if file is executed
   main()