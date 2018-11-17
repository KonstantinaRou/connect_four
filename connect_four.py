from players import Player
from Board import Board
# from players import remove_colors

def start_game():
    # initialize board

    # create players
    player = []
    colors = ['R','G','B','Y']
    player.append(Player(colors))
    player.append(Player(colors))
    board = Board()
    # play
    print(board.gameplay(player))


if __name__ == '__main__':
    start_game()
