
def start_game():

    board = initialize_board()
    while board is "RETRY":
        print("You entered wrong input, please enter only numbers bigger than 0")
        board = initialize_board()
    print(board.board)
    player1 = Player('R')
    player2 = Player('G')
    player1.move(board)
    player1.move(board)
    player1.move(board)
    print (board.board)


def initialize_board():
    try:
        x, y = [int(x) for x in input('Enter Grid Size (row, column):').split(',')]
        if x <= 0 or y <= 0:
            return "RETRY"

        grids = [['X'] * x for _ in range(y)]
        return Board(x, y, grids)

    except ValueError:
        return "RETRY"

class Board:
    # every board has specific size
    def __init__(self, x, y, board):
        self.x = x
        self.y = y
        self.board = board


class Player:

    def __init__(self, color):
        # every player has a color idendity
        self.color = color

    def move(self, board):
        board = board.board
        # make a move on the board, place the player's color inside the board
        column = int(input(" Place your disk at: (enter column)"))
        # check if column is out of bounds
        while column > len(board) or column < 0:
            print("Wrong input, try again")
            column = int(input("Place your disk at: (enter column)"))
        while board[0][column - 1] != 'X':
            print('slot', column, 'is full try again')
            column = int(input("Place your disk at: (enter column)"))
        else:
            # piece the disk inside the board
            column = column-1
            for slot in board[::-1]:
                if slot[column] == 'X':
                    slot[column] = self.color
                    return board






if __name__ == '__main__':
    start_game()
