
def start_game():

    board = initialize_board()
    while board is "RETRY":
        print("You entered wrong input, please enter only numbers bigger than 0")
        board = initialize_board()


def initialize_board():
    try:
        x, y = [int(x) for x in input('Enter Grid Size (row, column):').split(',')]
        if x <= 0 or y <= 0:
            return "RETRY"

        grids = [[0] * x for _ in range(y)]
        return grids

    except ValueError:
        return "RETRY"


if __name__ == '__main__':
    start_game()
