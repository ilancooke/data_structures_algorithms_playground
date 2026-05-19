# Adjacency list with three connected components:
# 1. A-B-C
# 2. D-E
# 3. F by itself
graph = {
    "A": ["B"],
    "B": ["A", "C"],
    "C": ["B"],
    "D": ["E"],
    "E": ["D"],
    "F": [],
}


def connected_components(graph):
    # Track every node we have already assigned to a component.
    visited = set()
    # Store each connected component as a list of nodes.
    components = []

    # The outer loop ensures we check every node in the graph.
    for node in graph:
        # If this node was already reached by an earlier traversal, skip it.
        if node in visited:
            continue

        # Starting a traversal from an unvisited node means we found a new component.
        component = []
        # Use DFS with a stack to explore everything connected to this node.
        stack = [node]

        # Explore all nodes reachable from the starting node.
        while stack:
            # Pop the most recently discovered node.
            current = stack.pop()

            # Skip nodes already processed.
            if current in visited:
                continue

            # Mark this node as part of the current component.
            visited.add(current)
            # Record this node in the current component.
            component.append(current)

            # Add unvisited neighbors so they can be explored.
            for neighbor in graph[current]:
                if neighbor not in visited:
                    stack.append(neighbor)

        # After the traversal finishes, the full component has been found.
        components.append(component)

    # Return a list of components, where each component is a list of connected nodes.
    return components


print(connected_components(graph))
