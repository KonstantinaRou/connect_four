from players import Player
from Board import Board


def start_game():
    # initialize board

    # create players
    player = []
    player.append(Player('R'))
    player.append(Player('G'))
    board = Board()
    # play
    print(board.gameplay(player))


if __name__ == '__main__':
    start_game()
