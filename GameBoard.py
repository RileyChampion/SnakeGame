from Snake import snake

class gameboard(object):
	"""docstring for gameboard"""
	def __init__(self):
		super(gameboard, self).__init__()
		self.gameboard = [[" " for _ in range(15)] for _ in range(15)] #create a 15 x 15 gameboard
		self._new_snake = snake()

		for location in self._new_snake.snake_array[:]:
			self.gameboard[location[0]][location[1]] = "S"

	def _clear_game_board(self) -> None:
		self.gameboard = [[" " for _ in range(15)] for _ in range(15)]

	def _update_game_board(self) -> None:
		self._clear_game_board()

		for location in self._new_snake.snake_array:
			self.gameboard[location[0]][location[1]] = "S"

	def turn_snake_left(self) -> None:
		self._new_snake.moveLeft()

	def turn_snake_right(self) -> None:
		self._new_snake.moveRight()

	def move_snake_forward(self) -> None:
		self._new_snake.moveSnakeForward()
		self._update_game_board()

		# if self._new_snake.head == self._apple_location:


	def _check_for_apple(self) -> bool:
		return True



		