from players import Player
from Board import Board


def start_game():

    # initialize colors
    colors = ['R', 'G', 'B', 'Y']
    # create players
    players = []
    players.append(Player(colors))
    players.append(Player(colors))

    # initialize board
    board = Board()
    # play
    print(board.gameplay(players))


if __name__ == '__main__':
    start_game()
