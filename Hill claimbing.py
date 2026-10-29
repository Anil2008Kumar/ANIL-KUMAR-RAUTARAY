#objective function
def objective_function(x):
  return -4*(x-5)**2+100

#hill climbing function
def hill_climbing(start, step_size, max_iterations):
  current = start
  current_value = objective_function(current)

  for i in range(max_iterations):
    left = current - step_size
    right = current + step_size
    left_value = objective_function(left)
    right_value = objective_function(right)

    # Move to the better neighbour
    if left_value > current_value:
      current = left
      current_value = left_value
    elif right_value > current_value:
      current = right
      current_value = right_value
    else:
      break # No better neighbor found, stop search

  return current, current_value

# Main program
start_point = float(input("Enter the starting point: "))
step = float(input("Enter the step size: "))
iterations = int(input("Enter maximum iterations: "))

best_position, best_value = hill_climbing(start_point, step, iterations)
print("\nBest position =", best_position)
print("Maximum value =", best_value)
