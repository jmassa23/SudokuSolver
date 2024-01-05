import sys


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
    
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            

            print(str(board[i][j]) + " ", end="")
        print("")

def isUsedInBox(board, boxRow, boxCol, val):
    for r in range(3):
        for c in range(3):
            if board[r + boxRow][c + boxCol] == val:
                return True
    return False

def isUsedInRow(board, row, val):
    for col in range(len(board[0])):
        if board[row][col] == val:
            return True
    return False

def isUsedInCol(board, col, val):
    for row in range(len(board)):
        if board[row][col] == val:
            return True
    return False

def isValid(board, row, col, val):
    return board[row][col] == 0 and \
        not isUsedInRow(board, row, val) and \
        not isUsedInCol(board, col, val) and \
        not isUsedInBox(board, row - row%3, col - col%3, val)

def findEmpty(board):
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == 0:
                return (r,c)
            
    return None

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




def main(args):
    board = [[0] * 9 for _ in range(9)]
    if solve(board):
        print_board(board)
    else:
        print("There is no solution for this board.")


if __name__ == "__main__":
    args = sys.argv
    main(args)