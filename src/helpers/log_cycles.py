import datetime

def log_cycles(graph, fn, label):
  start_time = datetime.datetime.now()

  cycles = fn(graph)

  end_time = datetime.datetime.now()

  time_diff = (end_time - start_time)

  execution_time = time_diff.total_seconds() * 1000

  cycles.sort(key=len)
  for index, cycle in enumerate(cycles):
    print(f'Cycle {index + 1}: {cycle}')
  print(f'took {execution_time}ms to run {label}')

  return cycles