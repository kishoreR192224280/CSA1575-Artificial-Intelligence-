def dfs_recursive(graph, node, visited=None):
    """Recursive implementation of DFS starting from the given node."""
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=" ")

    # Recursively visit all unvisited neighbors
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Start DFS from node 'A'
print("Recursive DFS traversal order:")
dfs_recursive(graph, 'A')
print()
