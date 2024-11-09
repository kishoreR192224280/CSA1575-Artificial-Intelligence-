import heapq

class PuzzleState:
    def __init__(self, board, empty_pos, moves=0, prev=None):
        self.board = board  
        self.empty_pos = empty_pos  
        self.moves = moves 
        self.prev = prev  
        self.priority = self.calculate_priority() 
    
    def calculate_priority(self):
        """Calculate the priority (f(n)) for A* search: f(n) = g(n) + h(n)."""
        return self.moves + self.manhattan_distance()
    
    def manhattan_distance(self):
        """Heuristic function: Manhattan distance to the goal."""
        distance = 0
        goal = {0: (2, 2), 1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1)}
        for i in range(9):
            if self.board[i] != 0:
                curr_pos = (i // 3, i % 3)
                goal_pos = goal[self.board[i]]
                distance += abs(curr_pos[0] - goal_pos[0]) + abs(curr_pos[1] - goal_pos[1])
        return distance

    def get_neighbors(self):
        """Return all possible states from the current state by moving the empty space."""
        neighbors = []
        row, col = self.empty_pos
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_board = self.board[:]
                new_empty_pos = (new_row, new_col)
                new_board[row * 3 + col], new_board[new_row * 3 + new_col] = new_board[new_row * 3 + new_col], new_board[row * 3 + col]
                neighbors.append(PuzzleState(new_board, new_empty_pos, self.moves + 1, self))
        
        return neighbors

    def is_goal(self):
        """Check if the current state is the goal state."""
        return self.board == [1, 2, 3, 4, 5, 6, 7, 8, 0]

def a_star(start_state):
    """Solve the 8-puzzle problem using A* search."""
    open_list = []
    closed_list = set()
    
    heapq.heappush(open_list, (start_state.priority, start_state))
    closed_list.add(tuple(start_state.board))
    
    while open_list:
        _, current_state = heapq.heappop(open_list)
        
        if current_state.is_goal():
            return current_state
        
        for neighbor in current_state.get_neighbors():
            if tuple(neighbor.board) not in closed_list:
                heapq.heappush(open_list, (neighbor.priority, neighbor))
                closed_list.add(tuple(neighbor.board))
    
    return None  

def print_solution(solution):
    """Print the solution path."""
    path = []
    while solution:
        path.append(solution.board)
        solution = solution.prev
    path.reverse()
    
    for step in path:
        for i in range(3):
            print(step[i*3:(i+1)*3])
        print()

if __name__ == "__main__":
    initial_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    empty_pos = (2, 2) 
    
    start_state = PuzzleState(initial_state, empty_pos)

    solution = a_star(start_state)
    
    if solution:
        print("Solution found!")
        print_solution(solution)
    else:
        print("No solution exists.")
