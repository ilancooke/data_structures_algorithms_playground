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
    # Store the order we visit nodes in, useful for learning/debugging.
    order = []

    def visit(node):
        # Base case: stop if this node was already processed.
        if node in visited:
            return

        # Mark the node as processed.
        visited.add(node)
        # Record that we visited this node.
        order.append(node)

        # Recursively visit each neighbor before returning.
        for neighbor in graph[node]:
            visit(neighbor)

    # Start the recursive traversal from the requested node.
    visit(start)
    # Return the full DFS traversal order.
    return order


print(dfs(graph, "A"))
