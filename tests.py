import unittest
from players import Player
from unittest.mock import patch
from unittest import mock
from io import StringIO
from Board import Board
from Board import getx_y
from Board import initialize_board


class PlayerTest(unittest.TestCase):
    @patch('players.Player.get_column' ,return_value = 1)
    def test_move(self, mock_col):
        board = [["X", "X", "X", "X"],
                 ["X", "X", "X", "X"],
                 ["X", "X", "X", "X"],
                 ["X", "X", "X", "X"]]

        expected_board = [["X", "X", "X", "X"],
                          ["X", "X", "X", "X"],
                          ["X", "X", "X", "X"],
                          ["R", "X", "X", "X"]]
        player = Player('R')
        self.assertEqual(player.move(board),expected_board)

    @patch('builtins.input', return_value = 'a')
    def test_get_Column_error(self, mock_input):
        board = [["X", "X", "X", "X"],
                 ["X", "X", "X", "X"],
                 ["X", "X", "X", "X"],
                 ["X", "X", "X", "X"]]
        player = Player('R')
        self.assertEqual(player.get_column(board), None)

    @patch('builtins.input', return_value = 1)
    def test_get_Column(self, mock_input):
        board = [["X", "X", "X", "X"],
                 ["X", "X", "X", "X"],
                 ["X", "X", "X", "X"],
                 ["X", "X", "X", "X"]]
        player = Player('R')
        self.assertEqual(player.get_column(board), 1)


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

    @patch('players.Player.get_column')
    def test_gameplay_with_winner(self, mock_moves):
        mock_moves.side_effect = [1,2,1,2,1,2,1]
        board = [["X", "X", "X", "X"],
                 ["X", "X", "X", "X"],
                 ["X", "X", "X", "X"],
                 ["X", "X", "X", "X"]]
        board = Board(board)
        player = []
        player.append(Player('R'))
        player.append(Player('G'))
        self.assertEqual(board.gameplay(player), "R")

    @patch('players.Player.get_column')
    def test_gameplay_withDraw(self, mock_moves):
        mock_moves.side_effect = [1,2,2,1]
        board = [["X", "X"],
                 ["X", "X"]]
        board = Board(board)
        player = []
        player.append(Player('R'))
        player.append(Player('G'))
        self.assertEqual(board.gameplay(player), "DRAW")


if __name__ == '__main__':
    unittest.main()
