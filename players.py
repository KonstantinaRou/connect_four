class Player:
    def __init__(self,colors):
        # every player has a color idendity

        self.color = (get_color_player(colors))
        while self.color is None:
            self.color =(get_color_player(colors))

    def move(self, board):
        """
        make a move inside the board, place the player's color inside the board

        :param board: list
        :return: list
        """
        column = self.get_column(board)
        while column is None:
            column = self.get_column(board)
        # piece the disk inside the board
        column = column-1
        for slot in board[::-1]:
            if slot[column] == 'X':
                slot[column] = self.color
                return board

    def get_column(self, board):
        """
        Get the column which the player wants to make a move

        :param board: list
        :return: int
        """
        try:
            print ("Player ", self.color, " Turn (enter column):​ ")
            column = int(input())
            # check if column is out of bounds
            while column > len(board[0]) or column <= 0:
                print("Wrong input, try again")
                print("Player ", self.color, " Turn (enter column):​ ")
                column = int(input())
            while board[0][column - 1] != 'X':
                print('slot', column, 'is full try again')
                print("Player ", self.color, " Turn (enter column):​ ")
                column = int(input())
        except ValueError:
            print ("Enter a number as column")
            return None
        return column


def get_color_player(colors):
    """
    Player chooses color from available colors

    :param colors: list
    :return: string
    """
    try:
        print("Available colors:", colors)

        color = input()
        if color == 'R' or color == "B" or color ==  "G" or color == "Y":
            colors.remove(color)
            return color
        else:
            return None
    except ValueError:
        return None
