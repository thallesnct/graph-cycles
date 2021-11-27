from .immutable import get_edge_alias

def generate_adjacency_list(graph, is_directed_graph = False):
  adjacency_list = { vertex: set() for vertex in graph['vertices'] }

  for (vertex_a, vertex_b) in graph['edges']:
    adjacency_list[vertex_a].add(vertex_b)

    if (is_directed_graph is False):
      adjacency_list[vertex_b].add(vertex_a)

  return adjacency_list

def generate_edge_path(vertices_path, is_directed_graph = False):
  edge_path = list()
  limit = len(vertices_path) - 1

  for index, vertex in enumerate(vertices_path):
    if (index == limit):
      return edge_path

    edge_path.append(get_edge_alias(vertex, vertices_path[index + 1], is_directed_graph))