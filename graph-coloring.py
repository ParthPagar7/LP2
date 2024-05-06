def is_safe(graph, color, v, colored):
  """
  This function checks if it's safe to assign color 'color' to vertex 'v' in the graph.
  It considers adjacent vertices and ensures none share the same color.
  """
  for i in range(len(graph[v])):
    if colored[i] == color and graph[v][i] == 1:
      return False
  return True

def backtrack(graph, m, colored, v, assignment):
  """
  This is the recursive backtracking function.
  It attempts to assign colors to all vertices one by one.
  If a conflict arises, it backtracks and tries a different color.
  """
  if v == len(graph):
    return True

  # Try all possible colors
  for c in range(1, m + 1):
    if is_safe(graph, c, v, colored):
      colored[v] = c  # Assign color
      assignment.append(c)  # Add assignment to track colors used

      # Recur for next vertex
      if backtrack(graph, m, colored, v + 1, assignment):
        return True
     
      # Backtrack if assignment doesn't lead to a solution
      colored[v] = 0  # Un-assign color
      assignment.pop()  # Remove assignment

  return False

def minimum_color(graph):
  """
  This function finds the minimum number of colors needed to color the graph
  using Branch and Bound technique. It calls the backtracking function with
  an initial upper bound (number of vertices) and keeps reducing it as solutions
  are found with fewer colors.
  """
  num_vertices = len(graph)
  result = float('inf')  # Initialize upper bound
  min_colors = 0  # Minimum colors found so far
  colored = [0] * num_vertices  # To store vertex colors
  assignment = []  # To track color assignments

  # Iterate through upper bound values (number of vertices to maximum colors)
  for m in range(1, num_vertices + 1):
    if backtrack(graph, m, colored, 0, assignment):
      result = min(result, m)  # Update upper bound if a solution is found
      min_colors = m  # Keep track of minimum colors found so far
      assignment.clear()  # Clear assignment for next iteration

  # Return minimum colors and colored vertex list
  return min_colors, colored

# Example usage
graph = [
  [0, 1, 1, 1],
  [1, 0, 1, 0],
  [1, 1, 0, 1],
  [1, 0, 1, 0],
]

min_colors, colored = minimum_color(graph)

print("Minimum colors needed:", min_colors)
print("Coloring of vertices:", colored)