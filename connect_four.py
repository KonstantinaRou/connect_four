
def start_game():

    # initialize board
    board = initialize_board()
    while board is "RETRY":
        print("You entered wrong input, please enter only numbers bigger than 0")
        board = initialize_board()
    # create players
    player = []
    player.append(Player('R'))
    player.append(Player('G'))
    # play
    print(gameplay(player, board))


def gameplay(player, board):
    # players take turns where they place their pieces inside the board
    # with every move, check if there is a winner
    # returns the winner or draw
    finish = False
    i = 0
    counter = 0
    winner = ''
    while not finish:
        counter +=1
        player[i].move(board)
        print("Turn: ", counter, "\n ", board)
        if check_horiz(board, player[i].color) is True or check_vertically(board, player[i].color) is True:
            winner = player[i]
            finish = True
            break
        player[i+1].move(board)
        if check_horiz(board, player[i+1].color) is True or check_vertically(board, player[i+1].color) is True:
            winner = player[i+1]
            finish = True
        print("Turn: ", counter, "\n", board)
        i = 0
        if check_board_is_full(board):
            return "DRAW"
    return winner.color


def check_board_is_full(board):
    # check if the board is full bu checking the heightest row
    row = board[0]
    for piece in row:
        if piece =='X':
            return False
    return True


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
                return True


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
                return True


def check_diagonical_up(board,color):
    # check / diagonal spaces
    for x in range(len(board) - 3):
        for y in range(3, len(board[0])):
            if board[x][y] == color and board[x + 1][y - 1] == color and board[x + 2][y - 2] == color and \
                    board[x + 3][y - 3] == color:
                return True


def check_diagonical_down(board,color):
    for x in range(len(board) - 3):
        for y in range(len(board[0]) - 3):
            if board[x][y] == color and board[x+1][y+1] == color and board[x+2][y+2] == color and \
                    board[x+3][y+3] == color:
                return True


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
