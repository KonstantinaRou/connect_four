from players import Player
from Board import Board


def start_game():

    # initialize colors
    colors = ['R', 'G', 'B', 'Y']
    # create players
    players = []
    print("Choose player ",1, " color: ")
    players.append(Player(colors))
    print("Choose player ",2, " color: ")
    players.append(Player(colors))

    # initialize board
    board = Board()
    # play
    print(board.gameplay(players))


if __name__ == '__main__':
    start_game()
