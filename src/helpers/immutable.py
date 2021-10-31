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