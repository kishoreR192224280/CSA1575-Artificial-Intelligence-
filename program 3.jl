from collections import deque

def water_jug_solver(capacity1, capacity2, target):
    """Solves the water jug problem using BFS."""
    # Initialize the queue with the initial state (0, 0)
    queue = deque([(0, 0)])  # (jug1, jug2)
    visited = set((0, 0))  # Track visited states to avoid repeats

    # Define possible operations as lambda functions
    operations = [
        lambda x, y: (capacity1, y),    # Fill jug1
        lambda x, y: (x, capacity2),    # Fill jug2
        lambda x, y: (0, y),            # Empty jug1
        lambda x, y: (x, 0),            # Empty jug2
        lambda x, y: (x - min(x, capacity2 - y), y + min(x, capacity2 - y)),  # Pour jug1 -> jug2
        lambda x, y: (x + min(y, capacity1 - x), y - min(y, capacity1 - x)),  # Pour jug2 -> jug1
    ]

    # BFS traversal
    steps = 0
    while queue:
        for _ in range(len(queue)):
            jug1, jug2 = queue.popleft()

            # Check if we reached the target
            if jug1 == target or jug2 == target:
                return steps

            # Apply each operation
            for operation in operations:
                new_state = operation(jug1, jug2)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append(new_state)
        steps += 1

    return -1  # If no solution found

# Example usage:
capacity1 = 4  # Capacity of the first jug
capacity2 = 3  # Capacity of the second jug
target = 2     # Target amount to measure

steps = water_jug_solver(capacity1, capacity2, target)
if steps != -1:
    print(f"The target amount of {target} liters can be measured in {steps} steps.")
else:
    print("It's not possible to measure the target amount with the given jugs.")
