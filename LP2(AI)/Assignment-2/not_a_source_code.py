def astar(start_node, goal_node):
  open_set = set([start_node])
  closed_set = set()
  
  g_score = {start_node:0}
  f_score = {start_node:start_node.heuristic(goal_node)}
  parent=0
  
  while open_set:
    current = min(open_set, key=lambda node:f_score[node])
    
    if current == goal_node:
      path = [current]
      while current in parent:
        current = parent[current]
        path.append(current)
        
      path.reverse()
      return path
    
    open_set.remove(current)
    closed_set.add(current)
    
    for neighbor in current_neighbors():
      if neighbor in closed_set:
        continue
        
      tentative_g_score = g_score[current]+current.distance(neighbour)
      
      if neightbor not in open_set:
        open_set.add(neighbor)
        
      elif tentative_g_score >= g_score[neighbor]:
        continue
        
      parent[neighbor] = current
      g_score[neighbor] = tentative_g_score
      f_score[neighbor] = tentative_g_score + neighbor.heuristic(goal_node)
      
  return None
