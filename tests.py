import unittest
from players import Player
from unittest.mock import patch
from unittest import mock
from io import StringIO
from Board import Board
from Board import initialize_board

class PlayerTest(unittest.TestCase):

    def run_test_move(self, given_answer , output):
        board = [["X", "X", "X", "X"],
                 ["X", "X", "X", "X"],
                 ["X", "X", "X", "X"],
                 ["X", "X", "X", "X"]]
        player = Player('R')
        with patch('builtins.input', column=given_answer), patch('sys.stdout', new=StringIO()) as fake_out:
            player.move(board)

        self.assertEqual(fake_out.getvalue().strip(), output)


    def testCorrectValue(self):
        expected_board = [["X", "X", "X", "X"],
                          ["X", "X", "X", "X"],
                          ["X", "X", "X", "X"],
                          ["R", "X", "X", "X"]]
        self.run_test_move('1', str(expected_board))


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

    @patch('Board.getx_y', return_value='4,4')
    def check_initializeBoard_true(self):
        board = [["X", "X", "X", "X"],
                 ["X", "X", "X", "X"],
                 ["X", "X", "X", "X"],
                 ["X", "X", "X", "X"]]
        self.assertEqual(initialize_board(),board)

    @patch('Board.getx_y', return_value='None,None')
    def check_initializeBoard_retry(self):
        self.assertEqual(initialize_board(),"RETRY")



if __name__ == '__main__':
    unittest.main()
