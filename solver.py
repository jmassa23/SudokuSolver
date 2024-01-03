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

def main(args):
    board = [[0] * 9 for _ in range(9)]
    print_board(board)


if __name__ == "__main__":
    args = sys.argv
    main(args)