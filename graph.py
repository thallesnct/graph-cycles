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

def copy_path_and_add_edge_path(vertex_a, vertex_b, path):
  new_path = path

  if (len(path) != 0):
    new_path = path.copy()

  if (vertex_a > vertex_b):
    new_path.add(int(f'{vertex_b}{vertex_a}'))
  else:
    new_path.add(int(f'{vertex_a}{vertex_b}'))

  return new_path

def is_path_in_cycle_list(path, cycle_list):
  is_in_list = False

  for path_arr in cycle_list:
    # if (len(path) > 3 and path[0] == 1 and path[1] == 4 and path[2] == 2 and path[3] == 1):
    #   print(f'path={path}')
    #   print(f'path_arr={path_arr}')

    if len(path_arr) != len(path):
      continue

    if sorted(path_arr) == sorted(path):
      is_in_list = True
  
  return is_in_list

def is_edge_path_in_cycle_list(edge_path, cycle_list):
  is_in_list = False

  for edge_set in cycle_list:
    if len(edge_set) != len(edge_path):
      continue

    set_diff = edge_set.difference(edge_path)

    if len(set_diff) == 0:
      is_in_list = True

  return is_in_list

def validate_and_add_to_lists(vertex, path, edge_path, all_cycles, all_edge_cycles):
  new_path = copy_path_and_add_vertex(vertex, path)
  new_edge_path = copy_path_and_add_edge_path(path[len(path)-1], vertex, edge_path)

  if not is_edge_path_in_cycle_list(new_edge_path, all_edge_cycles) and not is_path_in_cycle_list(new_path, all_cycles):
    all_cycles.append(new_path)
    all_edge_cycles.append(new_edge_path)

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

def search_cycle_with_size(vertex, adjancency_list, visited, all_cycles, all_edge_cycles, size, path = [], edge_path = set()):
  if (len(path) == size):
    return
  
  if (visited.get(vertex) is True):
    if len(path) + 1 == size and vertex is path[0]:
      validate_and_add_to_lists(vertex, path, edge_path, all_cycles, all_edge_cycles)
    return
  
  visited[vertex] = True
  new_path = copy_path_and_add_vertex(vertex, path)
  new_edge_path = edge_path

  if len(new_path) > 1:
    new_edge_path = copy_path_and_add_edge_path(path[len(path)-1], vertex, edge_path)

  for child in adjancency_list[vertex]:
    new_visited = visited.copy()
    search_cycle_with_size(child, adjancency_list, new_visited, all_cycles, all_edge_cycles, size, new_path, new_edge_path)

def find_cycles_by_permutation(graph):
  adjancency_list = calculate_adjancency_list(graph)

  all_cycles = list()
  all_edge_cycles = list()

  for length in range(4, len(graph['vertices']) + 2):
    for vertex in graph['vertices']:
      visited = dict()
      search_cycle_with_size(vertex, adjancency_list, visited, all_cycles, all_edge_cycles, length)

  return all_cycles

def find_cycles_by_traversal(graph):
  adjancency_list = calculate_adjancency_list(graph)

  all_cycles = list()
  all_edge_cycles = list()

  for vertex in graph['vertices']:
    visited = dict()

    dfs(vertex, adjancency_list, visited, all_cycles, all_edge_cycles)

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
  #   'vertices': list(range(1, 14)),
  #   'edges': ((1,2), (2,3), (3,4), (3,5), (4,6), (4,7), (5,6), (5,9), (6,10), (7,8), (10,11), (11,12), (11,13), (12,13))
  # }
  # graph = { 
  #   'vertices': list(range(1,9)),
  #   'edges': ((1,2), (2,3), (2,5), (3,4), (4,5), (5,6), (6,7), (6,8), (7,8))
  # }
  graph = { 
    'vertices': list(range(1, 7)),
    'edges': ((1,4), (1,2), (1,5), (2,3), (2,4), (2,5), (3,4), (3,5), (3,6), (4,6), (5,6))
  }

  # set_a == set_b

  # (2,3,5,2) = set_a {'23', '35', '25'}
  # (3,5,2,3) = set_b {'35', '25', '23'}

  # nomes das arestas = string contendo a origem e o destino da aresta ordenados de menor para maior


  start_time = datetime.datetime.now()

  traversal_cycles = find_cycles_by_traversal(graph)

  end_time = datetime.datetime.now()

  time_diff = (end_time - start_time)

  execution_time = time_diff.total_seconds() * 1000

  traversal_cycles.sort(key=len)
  for index, cycle in enumerate(traversal_cycles):
    print(f'Cycle {index + 1}: {cycle}')
  print(f'took {execution_time}ms to run find_all_cycles_by_traversal')

  start_time = datetime.datetime.now()

  permutation_cycles = find_cycles_by_permutation(graph)

  end_time = datetime.datetime.now()

  time_diff = (end_time - start_time)

  execution_time = time_diff.total_seconds() * 1000

  for index, cycle in enumerate(permutation_cycles):
    print(f'Cycle {index + 1}: {cycle}')
  print(f'took {execution_time}ms to run find_all_cycles_by_traversal')

  starting_text = 'Não há' if len(permutation_cycles) == len(traversal_cycles) else 'Há'
  print(f'{starting_text} divergencias encontradas entre os dois métodos de busca')

if __name__ == "__main__":
   # Runs main if file is executed
   main()