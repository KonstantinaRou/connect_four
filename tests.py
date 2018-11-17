import unittest
from players import Player
from unittest.mock import patch
from unittest import mock
from Board import Board
from Board import initialize_board
from players import get_color_player

class PlayerTest(unittest.TestCase):
    @patch('players.Player.get_column' ,return_value = 1)
    @patch('players.get_color_player', return_value='R')
    def test_move(self, mock_col,mockplayer):
        board = [["X", "X", "X", "X"],
                 ["X", "X", "X", "X"],
                 ["X", "X", "X", "X"],
                 ["X", "X", "X", "X"]]

        expected_board = [["X", "X", "X", "X"],
                          ["X", "X", "X", "X"],
                          ["X", "X", "X", "X"],
                          ["R", "X", "X", "X"]]
        colors = ['R', 'G', 'B', 'Y']
        player = Player(colors)
        self.assertEqual(player.move(board),expected_board)

    @patch('builtins.input', return_value = 'a')
    @patch('players.get_color_player', return_value='R')
    def test_get_Column_error(self, mock_input,mockplayer):
        board = [["X", "X", "X", "X"],
                 ["X", "X", "X", "X"],
                 ["X", "X", "X", "X"],
                 ["X", "X", "X", "X"]]
        colors = ['R', 'G', 'B', 'Y']
        player = Player(colors)
        self.assertEqual(player.get_column(board), None)

    @patch('builtins.input', return_value = 1)
    @patch('players.get_color_player', return_value='R')
    def test_get_Column(self, mock_input,mockplayer):
        board = [["X", "X", "X", "X"],
                 ["X", "X", "X", "X"],
                 ["X", "X", "X", "X"],
                 ["X", "X", "X", "X"]]
        colors = ['R', 'G', 'B', 'Y']
        player = Player(colors)
        self.assertEqual(player.get_column(board), 1)

    @patch('builtins.input', return_value="R")
    def test_get_color_player(self,mock_input):
        colors = ['R', 'G', 'B', 'Y']
        self.assertEqual(get_color_player(colors),"R")

    @patch('builtins.input', return_value="f")
    def test_get_color_player_none(self,mock_input):
        colors = ['R', 'G', 'B', 'Y']
        self.assertEqual(get_color_player(colors),None)




class BoardTest(unittest.TestCase):

    def test_check_horiz_false(self):
        mockboard= [["X", "X", "X", "X"],
                    ["X", "X", "X", "X"],
                    ["X", "X", "X", "X"],
                    ["X", "X", "X", "X"]]
        board = Board(mockboard)

        self.assertEqual(board.check_horiz('R'), False)

    def test_check_horiz_True(self):
        mockboard= [["X", "X", "X", "X"],
                    ["R", "R", "R", "R"],
                    ["X", "X", "X", "X"],
                    ["X", "X", "X", "X"]]
        board = Board(mockboard)

        self.assertEqual(board.check_horiz('R'), True)

    def test_check_horiz_dif_color(self):
        mockboard= [["X", "X", "X", "X"],
                    ["R", "R", "R", "R"],
                    ["X", "X", "X", "X"],
                    ["X", "X", "X", "X"]]
        board = Board(mockboard)

        self.assertEqual(board.check_horiz('G'), False)

    def test_check_vertically_True(self):
        mockboard= [["R", "X", "X", "X"],
                    ["R", "X", "X", "X"],
                    ["R", "X", "X", "X"],
                    ["R", "X", "X", "X"]]
        board = Board(mockboard)
        self.assertEqual(board.check_vertically('R'), True)

    def test_check_vertically_False(self):
        mockboard= [["R", "X", "X", "X"],
                    ["X", "X", "X", "X"],
                    ["R", "X", "X", "X"],
                    ["R", "X", "X", "X"]]
        board = Board(mockboard)
        self.assertEqual(board.check_vertically('R'), False)

    def test_check_vertically_col_dif(self):
        mockboard= [["R", "X", "X", "X"],
                    ["R", "X", "X", "X"],
                    ["R", "X", "X", "X"],
                    ["R", "X", "X", "X"]]
        board = Board(mockboard)
        self.assertEqual(board.check_vertically('G'), False)

    def test_check_diagoniacal_down_true(self):
        mockboard= [["R", "X", "X", "X"],
                    ["X", "R", "X", "X"],
                    ["R", "X", "R", "X"],
                    ["R", "X", "X", "R"]]
        board = Board(mockboard)
        self.assertEqual(board.check_diagonical_down('R'), True)

    def test_check_diagoniacal_down_False(self):
        mockboard= [["R", "X", "X", "X"],
                    ["X", "R", "X", "X"],
                    ["R", "X", "X", "X"],
                    ["R", "X", "X", "R"]]
        board = Board(mockboard)
        self.assertEqual(board.check_diagonical_down('R'), False)

    def test_check_diagoniacal_down_big_true(self):
        mockboard= [["X", "R", "X", "X", "X"],
                    ["X", "X", "R", "X", "X"],
                    ["R", "X", "X", "R", "X"],
                    ["R", "X", "X", "R", "R"]]
        board = Board(mockboard)
        self.assertEqual(board.check_diagonical_down('R'), True)

    def test_check_diagoniacal_up_true(self):
        mockboard= [["R", "X", "X", "R"],
                    ["X", "X", "R", "X"],
                    ["R", "R", "X", "X"],
                    ["R", "X", "X", "R"]]
        board = Board(mockboard)
        self.assertEqual(board.check_diagonical_up('R'), True)

    def test_check_diagoniacal_up_false(self):
        mockboard= [["R", "X", "X", "R"],
                    ["X", "X", "X", "X"],
                    ["R", "R", "X", "X"],
                    ["R", "X", "X", "R"]]
        board = Board(mockboard)
        self.assertEqual(board.check_diagonical_up('R'), False)

    def test_check_diagoniacal_up_big_true(self):
        mockboard= [["X", "X", "X", "X", "R"],
                    ["X", "X", "X", "R", "X"],
                    ["R", "X", "R", "R", "X"],
                    ["R", "R", "X", "X", "R"]]
        board = Board(mockboard)
        self.assertEqual(board.check_diagonical_up('R'), True)

    def test_check_board_is_full_true(self):
        mockboard= [["R", "R", "R", "R"],
                    ["R", "R", "R", "R"],
                    ["R", "R", "R", "R"],
                    ["R", "R", "R", "R"]]
        board = Board(mockboard)
        self.assertEqual(board.check_board_is_full(), True)

    def test_check_board_is_full_false(self):
        mockboard= [["R", "R", "X", "R"],
                    ["R", "R", "R", "R"],
                    ["R", "R", "R", "R"],
                    ["R", "R", "R", "R"]]
        board = Board(mockboard)
        self.assertEqual(board.check_board_is_full(), False)

    @mock.patch('Board.getx_y', return_value=(4,4))
    def test_initializeBoard_true(self,mock_board):
        board = [["X", "X", "X", "X"],
                 ["X", "X", "X", "X"],
                 ["X", "X", "X", "X"],
                 ["X", "X", "X", "X"]]
        self.assertEqual(initialize_board(), board)

    @patch('Board.getx_y', return_value=(None,None))
    def test_initializeBoard_retry(self,mock_board):
        self.assertEqual(initialize_board(), "RETRY")

    @patch('players.get_color_player')
    @patch('players.Player.get_column')
    def test_gameplay_with_winner(self, mock_moves,mock_players):
        mock_moves.side_effect = [1,2,1,2,1,2,1]
        mock_players.side_effect = ['R','G']
        board = [["X", "X", "X", "X"],
                 ["X", "X", "X", "X"],
                 ["X", "X", "X", "X"],
                 ["X", "X", "X", "X"]]
        board = Board(board)
        player = []
        colors = ['R', 'G', 'B', 'Y']
        player.append(Player(colors))
        player.append(Player(colors))
        self.assertEqual(board.gameplay(player), "Player R won the game!!")

    @patch('players.get_color_player')
    @patch('players.Player.get_column')
    def test_gameplay_withDraw(self, mock_moves, mock_players):
        mock_moves.side_effect = [1,2,2,1]
        mock_players.side_effect = ['R', 'G']
        board = [["X", "X"],
                 ["X", "X"]]
        board = Board(board)
        player = []
        colors = ['R', 'G', 'B', 'Y']
        player.append(Player(colors))
        player.append(Player(colors))
        self.assertEqual(board.gameplay(player), "DRAW")

    @patch('players.get_color_player', return_value='R')
    def search_for_four_pieces_true(self, mock_player):
        colors = ['R', 'G', 'B', 'Y']
        board = [["R", "R", "R", "R"],
                 ["X", "X", "X", "X"],
                 ["X", "X", "X", "X"],
                 ["X", "X", "X", "X"]]
        player = Player(colors)
        board = Board(board)
        self.assertEqual(board.search_for_four_pieces(player),True)


    @patch('players.get_color_player', return_value='R')
    def search_for_four_pieces_false(self, mock_player):
        colors = ['R', 'G', 'B', 'Y']
        board = [["R", "R", "X", "R"],
                 ["X", "X", "X", "X"],
                 ["X", "X", "X", "X"],
                 ["X", "X", "X", "X"]]
        player = Player(colors)
        board = Board(board)
        self.assertEqual(board.search_for_four_pieces(player),False)

if __name__ == '__main__':
    unittest.main()
