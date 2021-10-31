def generate_adjancency_list(graph):
  adjancency_list = { vertex: set() for vertex in graph['vertices'] }

  for (vertex_a, vertex_b) in graph['edges']:
    adjancency_list[vertex_a].add(vertex_b)
    adjancency_list[vertex_b].add(vertex_a)

  return adjancency_list