from collections import deque

# -------------------------------
# BFS Traversal Function
# -------------------------------
def BFS_Traversal(graph, start_node):

    # Step 1: Create an empty VISITED list
    visited = []

    # Step 2: Create a QUEUE and add the start node
    queue = deque([start_node])

    # Step 3: Continue until the queue is empty
    while queue:

        # a. Remove the first node from the queue
        current_node = queue.popleft()

        # b. If current_node is not visited
        if current_node not in visited:

            # i. Print the explored node
            print("Explore Node:", current_node)

            # ii. Add it to visited
            visited.append(current_node)

            # iii. Visit all neighbours
            for neighbour in graph[current_node]:

                # Add neighbour only if not visited and not already in queue
                if neighbour not in visited and neighbour not in queue:
                    queue.append(neighbour)

    # Step 4: Return visited list
    return visited


# -------------------------------
# Main Program
# -------------------------------
def main_program():

    print("----- Build Your Graph -----")

    # Create an empty dictionary
    student_graph = {}

    # Number of edges
    num_edges = int(input("How many edges (connections) does your graph have? "))

    print("Enter each edge separated by a space (Example: A B)")

    # Input edges
    for i in range(num_edges):

        u, v = input(f"Edge {i+1}: ").split()

        # Check and initialize nodes
        if u not in student_graph:
            student_graph[u] = []

        if v not in student_graph:
            student_graph[v] = []

        # Create undirected connection
        student_graph[u].append(v)
        student_graph[v].append(u)

    # Starting node
    start = input("Enter the starting node for BFS: ")

    # Print graph
    print("\nYour Graph Dictionary:")
    print(student_graph)

    # Perform BFS
    print("\nStarting BFS Traversal...\n")
    visited_nodes = BFS_Traversal(student_graph, start)

    # Print visited list
    print("\nVisited Nodes:", visited_nodes)


# -------------------------------
# Run Program
# -------------------------------
main_program()