    def print_board(board):
    """Print the chessboard with queens."""
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    for i in range(row):
        if board[i][col]:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j]:
            return False

    return True

def solve_n_queens(board, row):
    """Use backtracking to place queens on the board."""
    if row >= len(board):
        print_board(board)
        return True

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1

            if solve_n_queens(board, row + 1):
                return True

            board[row][col] = 0

    return False

def solve_8_queens():
    """Solve the 8-Queens problem and print one solution."""
    n = 8 
    board = [[0] * n for _ in range(n)]
    
    if not solve_n_queens(board, 0):
        print("No solution exists.")

solve_8_queens()
