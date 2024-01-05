import sys

# fill board with 0's or fill from input file
def fill_board(filename):
    if not filename:
        return [[0] * 9 for _ in range(9)]

    board = []
    with open(filename, 'r') as file:
        lines = file.readlines()

        # check num of rows in board
        if len(lines) != 9:
            return None

        for line in lines:
            row = []
            for num in line:
                if num != '\n':
                    row.append(int(num))
            
            # check each row length
            if len(row) != 9:
                return None 
            
            board.append(row)
    
    return board

# print the current contents of the board
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
    
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            print(str(board[i][j]) + " ", end="")
        print("")

# check if the value is already in this 3x3 box
def isUsedInBox(board, boxRow, boxCol, val):
    for r in range(3):
        for c in range(3):
            if board[r + boxRow][c + boxCol] == val:
                return True
    return False

# check if the value is already in this row
def isUsedInRow(board, row, val):
    for col in range(len(board[0])):
        if board[row][col] == val:
            return True
    return False

# check if the value is already in this column
def isUsedInCol(board, col, val):
    for row in range(len(board)):
        if board[row][col] == val:
            return True
    return False

# check if this place is value is valid in this position
# position needs to be equal to 0 (not already filled)
# position needs to not have this value in this row, column, or 3x3 box
def isValid(board, row, col, val):
    return board[row][col] == 0 and \
        not isUsedInRow(board, row, val) and \
        not isUsedInCol(board, col, val) and \
        not isUsedInBox(board, row - row%3, col - col%3, val)

# find the next empty position in the board
def findEmpty(board):
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == 0:
                return (r,c)
            
    return None

# recursively solve the sudoku board using backtracking
# if we can find another empty square, loop through values 1 through 9
# for each value, check if we can place it at the empty position
# if we can recurse to solve, if solve returns false then we are backtracking and need to try a different value at this position
def solve(board):
    find = findEmpty(board)
    if not find:
        return True
    
    row, col = find

    for val in range(1,10):
        if isValid(board, row, col, val):
            board[row][col] = val

            if solve(board):
                return True
            
            board[row][col] = 0

    return False

def main(filename):
    board = fill_board(filename)

    if not board:
        print("Error: Invalid board")
        exit(1)

    print("\nStarting board:")
    print_board(board)
    
    if solve(board):
        print("\nSolution:")
        print_board(board)
    else:
        print("There is no solution for this board.\n")

if __name__ == "__main__":
    args = sys.argv
    filename = args[1] if len(args) > 1 else None
    main(filename)