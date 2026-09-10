# objective function
def objective_function(x):
    return -4 * (x - 5) ** 2 + 100  # example function


# hill climbing function
def hill_climbing(start, step_size, max_iterations):
    current = start
    current_value = objective_function(current)

    for i in range(max_iterations):
        left = current - step_size
        right = current + step_size

        left_value = objective_function(left)
        right_value = objective_function(right)

        # move to the better neighbour
        if left_value > current_value:
            current = left
            current_value = left_value
        elif right_value > current_value:
            current = right
            current_value = right_value
        else:
            break

    return current, current_value


# main program
start = float(input("enter the starting value:"))
step_size = float(input("enter the step size:"))
max_iterations = int(input("enetr the maximuim iteration:"))

best_position, best_value = hill_climbing(start, step_size, max_iterations)

print("\nbest position=", best_position)
print("maximum value=", best_value)