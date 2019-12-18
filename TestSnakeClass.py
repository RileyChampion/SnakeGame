import unittest
from Snake import *

class TestingSnakeClass(unittest.TestCase):
    def test_initialize_a_snake(self):
        newSnake = snake()

        self.assertEqual(newSnake._length, 2)
        self.assertEqual(newSnake._direction, "east")
        self.assertEqual(newSnake.snake_array[0], [10,2])
        self.assertEqual(newSnake.snake_array[1], [10,3])

    def test_move_snake_forward(self):
        newSnake = snake()

        newSnake.moveForward()

        self.assertEqual(newSnake.snake_array[0], [10,3])
        self.assertEqual(newSnake.snake_array[1], [10,4])
        self.assertEqual(len(newSnake.snake_array), newSnake._length)
        self.assertEqual(newSnake.head, [10,4])
        self.assertEqual(newSnake.tail, [10,3])

    def test_change_direction_left_and_move_forward(self):
        """Hypothetically this shouldn't change the direction of the
           snake"""
        newSnake = snake()

        newSnake.moveLeft()

        newSnake.moveForward()

        self.assertEqual(newSnake.snake_array[0], [10,3])
        self.assertEqual(newSnake.snake_array[1], [10,4])
        self.assertEqual(len(newSnake.snake_array), newSnake._length)
        self.assertEqual(newSnake.head, [10,4])
        self.assertEqual(newSnake.tail, [10,3])
        
    def test_change_direction_right_and_move_forward(self):
        """Hypothetically this shouldn't change the direction of the
           snake"""
        newSnake = snake()

        newSnake.moveRight()

        newSnake.moveForward()

        self.assertEqual(newSnake.snake_array[0], [10,3])
        self.assertEqual(newSnake.snake_array[1], [10,4])
        self.assertEqual(len(newSnake.snake_array), newSnake._length)
        self.assertEqual(newSnake.head, [10,4])
        self.assertEqual(newSnake.tail, [10,3])

    def test_change_direction_up_and_move_forward(self):
        """This should change the direction of the snake and move it
           up"""
        newSnake = snake()

        newSnake.moveUp()

        newSnake.moveForward()

        self.assertEqual(newSnake.snake_array[0], [10,3])
        self.assertEqual(newSnake.snake_array[1], [9,3])
        self.assertEqual(len(newSnake.snake_array), newSnake._length)
        self.assertEqual(newSnake.head, [9,3])
        self.assertEqual(newSnake.tail, [10,3])

    def test_change_direction_down_and_move_forward(self):
        """This should change the direction of the snake and move it
           down"""
        newSnake = snake()

        newSnake.moveDown()

        newSnake.moveForward()

        self.assertEqual(newSnake.snake_array[0], [10,3])
        self.assertEqual(newSnake.snake_array[1], [11,3])
        self.assertEqual(len(newSnake.snake_array), newSnake._length)
        self.assertEqual(newSnake.head, [11,3])
        self.assertEqual(newSnake.tail, [10,3])
        
        


if __name__ == '__main__':
	unittest.main()
