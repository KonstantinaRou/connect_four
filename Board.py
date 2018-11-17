
class Board:
    def __init__(self, board=None):
        if board is None:
            self.board = initialize_board()
            while self.board is "RETRY":
                print("You entered wrong input, please enter only numbers bigger than 0")
                self.board = initialize_board()
        else:
            self.board = board

    def gameplay(self, player):
        # players take turns where they place their pieces inside the board
        # with every move, check if there is a winner
        # returns the winner or draw
        board = self.board
        finish = False
        i = 0
        counter = 0
        winner = ''
        while not finish:
            counter += 1
            player[i].move(board)
            print("Turn: ", player[i].color, counter, "\n ", board)
            if self.check_horiz(player[i].color) is True or self.check_vertically(player[i].color) is True \
                    or self.check_diagonical_up(player[i].color) is True \
                    or self.check_diagonical_down(player[i].color):
                winner = player[i]
                finish = True
                break
            player[i + 1].move(board)
            if self.check_horiz(player[i + 1].color) is True or self.check_vertically(player[i + 1].color) is True \
                    or self.check_diagonical_up(player[i + 1].color) is True \
                    or self.check_diagonical_down(player[i + 1].color):
                winner = player[i + 1]
                finish = True
            print("Turn: ", player[i + 1].color, counter, "\n", board)
            i = 0
            if self.check_board_is_full():
                return "DRAW"
        return winner.color

    def check_horiz(self, color):
        board = self.board
        # check inside the board horizonadly for 4 continious same color pieces
        for row in board:
            iter_row = iter(row)
            count = 1
            next(iter_row, 0)
            for column in row:
                if column == next(iter_row, 0) and column == color:
                    count += 1
                if count == 4:
                    return True
        return False

    def check_vertically(self, color):
        board = self.board
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
        return False

    def check_diagonical_up(self, color):
        board = self.board
        # check / diagonal spaces
        for x in range(len(board) - 3):
            for y in range(3, len(board[0])):
                if board[x][y] == color and board[x + 1][y - 1] == color and board[x + 2][y - 2] == color and \
                        board[x + 3][y - 3] == color:
                    return True
        return False

    def check_diagonical_down(self, color):
        board = self.board
        for x in range(len(board) - 3):
            for y in range(len(board[0]) - 3):
                if board[x][y] == color and board[x + 1][y + 1] == color and board[x + 2][y + 2] == color and \
                        board[x + 3][y + 3] == color:
                    return True
        return False

    def check_board_is_full(self):
        board = self.board
        # check if the board is full bu checking the heightest row
        row = board[0]
        for piece in row:
            if piece == 'X':
                return False
        return True


def initialize_board():
    # create the board depending on users input

        x,y = getx_y()
        if x is None or y is None:
            return "RETRY"
        grids = [['X'] * x for _ in range(y)]
        return grids


def getx_y():
    try:
        x, y = [int(x) for x in input('Enter Grid Size (x, y):').split(',')]
        if x <= 0 or y <= 0:
            return None, None
        return x, y
    except ValueError:
        return None, None
