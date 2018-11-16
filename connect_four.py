
def start_game():

    board = initialize_board()
    while board is "RETRY":
        print("You entered wrong input, please enter only numbers bigger than 0")
        board = initialize_board()
    print(len(board[0]))
    player1 = Player('R')
    player2 = Player('G')
    player1.move(board)
    player2.move(board)
    player1.move(board)
    player2.move(board)
    player1.move(board)
    player2.move(board)
    player1.move(board)
    print (check_vertically(board,player1.color))
    print(board)


def initialize_board():
    # create the board depending on users input
    try:
        x, y = [int(x) for x in input('Enter Grid Size (x, y):').split(',')]
        if x <= 0 or y <= 0:
            return "RETRY"

        grids = [['X'] * x for _ in range(y)]
        return grids

    except ValueError:
        return "RETRY"


def check_horiz(board, color):
    # check inside the board horizonadly for 4 continious same color pieces
    for row in board:
        iter_row = iter(row)
        count = 1
        next(iter_row, 0)
        for column in row:
            if column == next(iter_row,0) and column == color:
                count += 1
            if count == 4:
                return color, " is winner!"


def check_vertically(board,color):
    # check inside the board vertically for 4 continious same color pieces
    cols = zip(*board)

    for row in cols:
        iter_row = iter(row)
        count = 1
        next(iter_row, 0)
        for column in row:
            if column == next(iter_row, 0) and column == color:
                count += 1
            if count == 4:
                return color, " is winner!"




class Player:
    def __init__(self, color):
        # every player has a color idendity
        self.color = color

    def move(self, board):
        # make a move on the board, place the player's color inside the board
        column = int(input(" Place your disk at: (enter column)"))
        # check if column is out of bounds
        while column > len(board[0]) or column <= 0:
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
