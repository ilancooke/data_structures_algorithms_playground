# Adjacency list: each node maps to the nodes directly connected to it.
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}


def dfs(graph, start):
    # Track nodes we have already processed so we do not loop forever in cycles.
    visited = set()
    # DFS with a stack: last node added is the first node processed.
    stack = [start]
    # Store the order we visit nodes in, useful for learning/debugging.
    order = []

    # Keep going while there are discovered nodes waiting to be processed.
    while stack:
        # Remove from the end/top of the stack.
        node = stack.pop()

        # If this node was already processed, skip it.
        if node in visited:
            continue

        # Mark the node as processed.
        visited.add(node)
        # Record that we visited this node.
        order.append(node)

        # Add unvisited neighbors to the stack.
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)

    # Return the full DFS traversal order.
    return order


print(dfs(graph, "A"))
