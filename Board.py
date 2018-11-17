
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
        """
        :param player : list
        players take turns where they place their pieces inside the board
        with every move, check if there is a winner
        returns the winner or draw

        """
        board = self.board
        finish = False
        i = 0
        counter = 0
        winner = ''
        while not finish:
            counter += 1
            player[i].move(board)
            print("Turn: ", player[i].color, counter, "\n ", board)
            if self.search_for_four_pieces(player[i]) is True:
                winner = player[i]
                break
            player[i + 1].move(board)
            if self.search_for_four_pieces(player[i+1]) is True:
                winner = player[i + 1]
                finish = True
            print("Turn: ", player[i + 1].color, counter, "\n", board)
            i = 0
            if self.check_board_is_full():
                return "DRAW"
        return winner.color

    def search_for_four_pieces(self, player):
        """

        :param player: Player object
        :return: Boolean

        searches for a line vertically/horizontally/diagonally with four discs
        """
        if self.check_horiz(player.color) is True or self.check_vertically(player.color) is True \
                or self.check_diagonical_up(player.color) is True \
                or self.check_diagonical_down(player.color):
            return True
        else:
            return False

    def check_horiz(self, color):
        """
        :param color: string
        :return: Boolean
        searches for a line horizontally with four discs

        """
        board = self.board

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
        """
           :param color: string
           :return: Boolean
           searches for a line vertically with four discs


        """
        board = self.board

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
        """

        :param color: string
        :return: Boolean
        searches for a line diagonally (/) with four discs
        """
        board = self.board
        # check / diagonal spaces
        for x in range(len(board) - 3):
            for y in range(3, len(board[0])):
                if board[x][y] == color and board[x + 1][y - 1] == color and board[x + 2][y - 2] == color and \
                        board[x + 3][y - 3] == color:
                    return True
        return False

    def check_diagonical_down(self, color):
        """

        :param color: string
        :return: Boolean
        searches for a line diagonally (\) with four discs
        """
        # check \ diagonal spaces
        board = self.board
        for x in range(len(board) - 3):
            for y in range(len(board[0]) - 3):
                if board[x][y] == color and board[x + 1][y + 1] == color and board[x + 2][y + 2] == color and \
                        board[x + 3][y + 3] == color:
                    return True
        return False

    def check_board_is_full(self):
        """

        :return: Boolean

        Checks if a board is full

        """
        board = self.board
        # check if the board is full bu checking the heightest row
        row = board[0]
        for piece in row:
            if piece == 'X':
                return False
        return True


def initialize_board():

    """
    creates a board depending on users input
    :return: list
    """
    x,y = getx_y()
    if x is None or y is None:
        return "RETRY"
    grids = [['X'] * x for _ in range(y)]
    return grids


def getx_y():
    """
    Gets the width and  the height from the user
    :return:  tuple
    """
    try:
        x, y = [int(x) for x in input('Enter Grid Size (x, y):').split(',')]
        if x <= 0 or y <= 0:
            return None, None
        return x, y
    except ValueError:
        return None, None
