from collections import deque


# Adjacency list: each node maps to the nodes directly connected to it.
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}


def bfs(graph, start):
    # Track nodes we have already processed so we do not loop forever in cycles.
    visited = set()
    # BFS uses a queue: first node added is the first node processed.
    queue = deque([start])
    # Store the order we visit nodes in, useful for learning/debugging.
    order = []

    # Keep going while there are discovered nodes waiting to be processed.
    while queue:
        # Remove from the left/front of the queue.
        node = queue.popleft()

        # If this node was already processed, skip it.
        if node in visited:
            continue

        # Mark the node as processed.
        visited.add(node)
        # Record that we visited this node.
        order.append(node)

        # Add unvisited neighbors to the back of the queue.
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)

    # Return the full BFS traversal order.
    return order


print(bfs(graph, "A"))
