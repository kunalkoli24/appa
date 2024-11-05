#  Design n-Queens matrix having first Queen placed. Use backtracking to place Queens to generate the 
# final n-queen‘s matrix

def print_board(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print("\n")

def is_safe(board, row, col, N):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True

# Recursive function to solve N-Queens using backtracking
def solve_nqueens(board, row, N):
    if row == N:
        return True  # All queens are placed

    # Try placing queen in each column for the current row
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1  # Place queen
            if solve_nqueens(board, row + 1, N):
                return True
            board[row][col] = 0  # Backtrack

    return False

def n_queens_with_fixed_start(N):
    # Initialize the board
    board = [[0 for _ in range(N)] for _ in range(N)]

    # Incorrect initial placement: place the first queen at top-left corner
    board[0][0] = 1
    print("Initial Board with Incorrect Placement:")
    print_board(board)

    # Reset board and use backtracking to find the correct solution
    board = [[0 for _ in range(N)] for _ in range(N)]
    if solve_nqueens(board, 0, N):  # Start solving from the first row
        print("Final Correct Solution:")
        print_board(board)
    else:
        print("No solution exists.")

# Get user input for N
N = int(input("Enter the size of the board (N): "))
n_queens_with_fixed_start(N)
