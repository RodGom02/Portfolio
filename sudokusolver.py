def print_board(board):
    """Prints the Sudoku board in a readable format."""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j], end=" ")
        print()


def find_empty(board):
    """Finds an empty cell (marked as 0) in the Sudoku board."""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)  # Return row and column index of empty cell
    return None


def is_valid(board, num, position):
    """Checks if placing 'num' at 'position' is valid according to Sudoku rules."""
    row, col = position

    # Check the row
    if num in board[row]:
        return False

    # Check the column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check the 3x3 sub-grid
    box_x, box_y = col // 3, row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num:
                return False

    return True


def solve_sudoku(board):
    """Solves the Sudoku board using backtracking."""
    empty_cell = find_empty(board)

    if not empty_cell:
        return True  # Puzzle is solved!

    row, col = empty_cell

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num  # Place the number

            if solve_sudoku(board):  # Recursively try to solve the rest
                return True

            board[row][col] = 0  # Reset on failure (Backtracking)

    return False  # No solution found


# Sample Sudoku puzzle (0 represents empty spaces)
sudoku_board = [
    [0, 0, 6, 0, 0, 9, 0, 0, 0],
    [1, 3, 0, 0, 0, 0, 0, 0, 4],
    [0, 0, 5, 0, 0, 6, 0, 0, 0],
    [0, 1, 0, 8, 7, 0, 9, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 5, 0],
    [0, 2, 9, 0, 0, 5, 3, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0],
    [0, 0, 0, 5, 4, 0, 0, 0, 1],
    [0, 0, 0, 0, 3, 8, 0, 0, 0]
]

print("Original Sudoku Board:")
print_board(sudoku_board)

if solve_sudoku(sudoku_board):
    print("\nSolved Sudoku Board:")
    print_board(sudoku_board)
else:
    print("\nNo solution exists!")
