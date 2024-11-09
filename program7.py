from collections import deque

def bfs(graph, start_node):
    """Perform BFS traversal from the start_node and print each visited node."""
    # Initialize the BFS queue and the set of visited nodes
    queue = deque([start_node])
    visited = set([start_node])

    print("BFS traversal order:")
    # Perform BFS
    while queue:
        # Dequeue a node from the front of the queue
        node = queue.popleft()
        print(node, end=" ")

        # Add all unvisited neighbors to the queue
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Start BFS from node 'A'
bfs(graph, 'A')
