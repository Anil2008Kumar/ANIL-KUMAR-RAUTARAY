def dfs(graph, start_node):
    visited = []
    stack = [start_node]

    while stack:
        current_node = stack.pop()

        if current_node not in visited:
            print(f"Exploring node: {current_node}")
            visited.append(current_node)

            # Add neighbours in reverse order so traversal follows input order
            for neighbor in reversed(graph.get(current_node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

    return visited


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

        # Create nodes if they don't exist
        if u not in student_graph:
            student_graph[u] = []

        if v not in student_graph:
            student_graph[v] = []

        # Undirected graph
        student_graph[u].append(v)
        student_graph[v].append(u)

    # Starting node
    start = input("Enter the starting node for DFS: ")

    # Check if start node exists
    if start not in student_graph:
        print("Starting node does not exist in the graph!")
        return

    # Print graph
    print("\nGraph Dictionary:")
    print(student_graph)

    # Perform DFS
    print("\nStarting DFS Traversal...\n")
    visited_nodes = dfs(student_graph, start)

    # Print visited list
    print("\nVisited Nodes:", visited_nodes)


# -------------------------------
# Run Program
# -------------------------------
if __name__ == "__main__":
    main_program()