import unittest
from GameBoard import *

class TestingGameBoard(unittest.TestCase):

    def test_initialize_gameboard(self):
        new_game_board = gameboard()

        check_game_board = [[" " for _ in range(15)] for _ in range(15)]

        check_game_board[10][2] = "S"
        check_game_board[10][3] = "S"

        check_game_board[new_game_board._apple_location[0]][new_game_board._apple_location[1]] = "A"

        self.assertEqual(new_game_board.gameboard, check_game_board)

    def test_move_snake_forward_on_gameboard(self):
        new_game_board = gameboard()

        check_game_board = [[" " for _ in range(15)] for _ in range(15)]

        check_game_board[10][3] = "S"
        check_game_board[10][4] = "S"

        new_game_board.move_snake_forward()

        check_game_board[new_game_board._apple_location[0]][new_game_board._apple_location[1]] = "A"

        self.assertEqual(new_game_board.gameboard, check_game_board)

    def test_move_snake_forward_on_gameboard(self):
        new_game_board = gameboard()

        check_game_board = [[" " for _ in range(15)] for _ in range(15)]

        check_game_board[10][3] = "S"
        check_game_board[10][4] = "S"

        new_game_board.move_snake_forward()

        check_game_board[new_game_board._apple_location[0]][new_game_board._apple_location[1]] = "A"

        self.assertEqual(new_game_board.gameboard, check_game_board)

    def test_turn_snake_up_and_move_snake_forward_on_gameboard(self):
        new_game_board = gameboard()

        check_game_board = [[" " for _ in range(15)] for _ in range(15)]

        check_game_board[10][3] = "S"
        check_game_board[9][3] = "S"

        new_game_board.turn_snake_up()

        new_game_board.move_snake_forward()

        check_game_board[new_game_board._apple_location[0]][new_game_board._apple_location[1]] = "A"

        self.assertEqual(new_game_board.gameboard, check_game_board)

    def test_turn_snake_down_and_move_snake_forward_on_gameboard(self):
        new_game_board = gameboard()

        check_game_board = [[" " for _ in range(15)] for _ in range(15)]

        check_game_board[10][3] = "S"
        check_game_board[11][3] = "S"

        new_game_board.turn_snake_down()

        new_game_board.move_snake_forward()

        check_game_board[new_game_board._apple_location[0]][new_game_board._apple_location[1]] = "A"

        self.assertEqual(new_game_board.gameboard, check_game_board)

    def test_move_toward_apple_increase_snake_size(self):
        new_game_board = gameboard()

        check_game_board = [[" " for _ in range(15)] for _ in range(15)]

        old_apple_location = [10,4]

        new_game_board._apple_location = [10, 4]

        check_game_board[10][2] = "S"
        check_game_board[10][3] = "S"
        check_game_board[10][4] = "S"
        new_game_board.move_snake_forward()

        for arr in check_game_board:
            print(arr)

        check_game_board[new_game_board._apple_location[0]][new_game_board._apple_location[1]] = "A"

        
        self.assertEqual(new_game_board.gameboard, check_game_board)
        self.assertEqual(new_game_board._new_snake._length, 3)

if __name__ == '__main__':
    unittest.main()
