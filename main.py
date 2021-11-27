from src.permutation import find_cycles_by_permutation
from src.traversal import find_cycles_by_traversal
from src.disjoint_paths import find_disjoint_paths
from src.helpers.log import log_cycles, log_paths


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
  # Directed graph
  directed_graph = { 
    'vertices': list(range(1, 7)),
    'edges': ((1,4), (1,2), (1,5), (2,3), (2,4), (2,5), (3,6), (4,3), (4,6), (5,3), (5,6))
  }

  print('--------- OPERACOES SOBRE CICLOS ---------')
  traversal_cycles = log_cycles(graph, fn = find_cycles_by_traversal, label = 'find_all_cycles_by_traversal')

  permutation_cycles = log_cycles(graph, fn = find_cycles_by_permutation, label = 'find_all_cycles_by_permutation')

  starting_text = 'Não há' if len(permutation_cycles) == len(traversal_cycles) else 'Há'
  print(f'{starting_text} divergencias encontradas entre os dois métodos de busca')

  print('--------- OPERACOES SOBRE CAMINHOS ---------')
  log_paths(fn = lambda: find_disjoint_paths(directed_graph, 1, 6), label = 'find_all_disjoint_paths')

if __name__ == "__main__":
   # Runs main if file is executed
   main()