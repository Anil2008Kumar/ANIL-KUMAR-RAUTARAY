def water_jug(capacity1, capacity2, target):
    queue = [(0, 0, [])]
    visited = set()

    while queue:
        jug1, jug2, path = queue.pop(0)

        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))
        path = path + [(jug1, jug2)]

        if jug1 == target or jug2 == target:
            return path

        next_states = [
            (capacity1, jug2),  # Fill jug 1
            (jug1, capacity2),  # Fill jug 2
            (0, jug2),          # Empty jug 1
            (jug1, 0),          # Empty jug 2
        ]

        # Pour jug 1 into jug 2
        amount = min(jug1, capacity2 - jug2)
        next_states.append((jug1 - amount, jug2 + amount))

        # Pour jug 2 into jug 1
        amount = min(jug2, capacity1 - jug1)
        next_states.append((jug1 + amount, jug2 - amount))

        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], path))

    return None


jug1 = int(input("Enter capacity of jug 1: "))
jug2 = int(input("Enter capacity of jug 2: "))
target = int(input("Enter target amount: "))

solution = water_jug(jug1, jug2, target)

if solution:
    print("\nSteps to reach the target:")
    for step in solution:
        print(step)
else:
    print("No solution exists")

      
     
       

