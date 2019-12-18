import unittest
from GameBoard import *

class TestingGameBoard(unittest.TestCase):

    def test_initialize_gameboard(self):
        new_game_board = gameboard()

        check_game_board = [[" " for _ in range(15)] for _ in range(15)]

        check_game_board[10][2] = "S"
        check_game_board[10][3] = "S"

        for arr in check_game_board:
            print(arr)

        self.assertEqual(new_game_board.gameboard, check_game_board)

    def test_move_snake_forward_on_game_board

        
if __name__ == '__main__':
    unittest.main()
