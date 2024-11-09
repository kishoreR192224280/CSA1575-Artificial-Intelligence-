from collections import deque

# Possible moves for the vacuum cleaner (up, down, left, right)
MOVES = {
    'UP': (-1, 0),
    'DOWN': (1, 0),
    'LEFT': (0, -1),
    'RIGHT': (0, 1)
}

def is_valid_position(x, y, grid):
    """Check if the position is within the bounds of the grid."""
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

def is_goal_state(grid):
    """Check if all cells in the grid are clean."""
    return all(cell == 'Clean' for row in grid for cell in row)

def apply_action(grid, position, action):
    """Apply an action and return the new grid and position."""
    x, y = position
    new_grid = [row[:] for row in grid]  # Copy the grid
    if action == 'SUCK':
        new_grid[x][y] = 'Clean'
    else:
        dx, dy = MOVES[action]
        nx, ny = x + dx, y + dy
        if is_valid_position(nx, ny, new_grid):
            return new_grid, (nx, ny)
    return new_grid, position

def vacuum_cleaner_bfs(grid, start_position):
    """Solve the Vacuum Cleaner Problem using BFS."""
    queue = deque([(grid, start_position, [])])  # (grid, position, path)
    visited = set()
    visited.add((tuple(tuple(row) for row in grid), start_position))
    
    while queue:
        current_grid, position, path = queue.popleft()
        
        # Check if all cells are clean
        if is_goal_state(current_grid):
            return path

        # Perform 'SUCK' action if the current cell is dirty
        x, y = position
        if current_grid[x][y] == 'Dirty':
            new_grid, new_position = apply_action(current_grid, position, 'SUCK')
            new_state = (tuple(tuple(row) for row in new_grid), new_position)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_grid, new_position, path + ['SUCK']))

        # Try moving in all four directions
        for action in MOVES.keys():
            new_grid, new_position = apply_action(current_grid, position, action)
            new_state = (tuple(tuple(row) for row in new_grid), new_position)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_grid, new_position, path + [action]))

    return None  # No solution found

def print_solution(solution):
    """Print the solution path."""
    if solution is None:
        print("No solution found.")
    else:
        print("Solution steps:")
        for step in solution:
            print(step)
        print("All cells are clean!")

# Example grid (2x2)
initial_grid = [
    ['Dirty', 'Dirty'],
    ['Clean', 'Dirty']
]
start_position = (0, 0)  # Starting at the top-left corner

# Solve the problem
solution = vacuum_cleaner_bfs(initial_grid, start_position)
print_solution(solution)
