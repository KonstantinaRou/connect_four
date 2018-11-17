class Player:
    def __init__(self, color):
        # every player has a color idendity
        self.color = color

    def move(self, board):
        # make a move on the board, place the player's color inside the board
        column = self.get_column(board)
        while column is None:
            column = self.get_column(board)
        # piece the disk inside the board
        column = column-1
        for slot in board[::-1]:
            if slot[column] == 'X':
                slot[column] = self.color
                print(board)
                return board

    def get_column(self,board):
        try:
            print (board)
            column = int(input(" Place your disk at: (enter column)"))
            # check if column is out of bounds
            while column > len(board[0]) or column <= 0:
                print("Wrong input, try again")
                column = int(input("Place your disk at: (enter column)"))
            while board[0][column - 1] != 'X':
                print('slot', column, 'is full try again')
                column = int(input("Place your disk at: (enter column)"))
        except ValueError:
            print ("Enter a number as column")
            return None
        return column
