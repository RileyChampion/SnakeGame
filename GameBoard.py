from Snake import snake
from random import randint

class gameboard(object):
	"""docstring for gameboard"""
	def __init__(self):
		super(gameboard, self).__init__()
		self.gameboard = [[" " for _ in range(15)] for _ in range(15)] #create a 15 x 15 gameboard
		self._new_snake = snake()
		while True:
			self._apple_location = [randint(0,14), randint(0,14)]
			if self._apple_location != [10,3] or self._apple_location != [10,2]:
				break

		for location in self._new_snake.snake_array[:]:
			self.gameboard[location[0]][location[1]] = "S"

		self.gameboard[self._apple_location[0]][self._apple_location[1]] = "A"

	def _clear_game_board(self) -> None:
		self.gameboard = [[" " for _ in range(15)] for _ in range(15)]

	def _update_game_board(self) -> None:
		self._clear_game_board()
		
		for location in self._new_snake.snake_array:
			self.gameboard[location[0]][location[1]] = "S"

		self.gameboard[self._apple_location[0]][self._apple_location[1]] = "A"

	def turn_snake_up(self) -> None:
		self._new_snake.moveUp()

	def turn_snake_down(self) -> None:
		self._new_snake.moveDown()

	def turn_snake_left(self) -> None:
		self._new_snake.moveLeft()

	def turn_snake_right(self) -> None:
		self._new_snake.moveRight()

	def move_snake_forward(self) -> None:
		self._new_snake.moveForward()
		if self._check_for_apple():
			self._new_snake.eatApple()
			self._new_apple_location()
		self._update_game_board()

		# if self._new_snake.head == self._apple_location:
	def _check_for_apple(self) -> bool:
		if self._new_snake.head == self._apple_location:
			return True
		return False

	def _new_apple_location(self) -> None:
		while True:
			self._apple_location = [randint(0,14),randint(0,14)]
			if self._apple_location not in self._new_snake.snake_array:
				break