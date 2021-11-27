def copy_path_and_add_vertex(vertex, path):
  new_path = path.copy()
  new_path.append(vertex)

  return new_path

def get_edge_alias(origin, target, is_directed = False):
  if (is_directed is True or origin < target):
    return f'{origin}{target}'

  return f'{target}{origin}'

def copy_path_and_add_edge_path(vertex_a, vertex_b, path, is_directed = False):
  new_path = path

  if (len(path) != 0):
    new_path = path.copy()

  new_path.add(get_edge_alias(vertex_a, vertex_b, is_directed))

  return new_path