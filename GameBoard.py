#import Snake

class gameboard(object):
	"""docstring for gameboard"""
	def __init__(self, newSnake):
		super(gameboard, self).__init__()
		self.gameboard = [[" " for _ in range(15)] for _ in range(15)] #create a 15 x 15 gameboard
		self.snake = newSnake

		for location in snake.snake_array:
			gameboard[location[0]][location[1]] = "S"

	def _clearGameBoard(self):
		self.gameboard = [[" " for _ in range(15)] for _ in range(15)]

	def _updateGameBoard(self):
		self._clearGameBoard()

		for location in snake.snake_array:
			gameboard[location[0]][location[1]] = "S"

	def turnSnakeLeft(self):
		newSnake.moveLeft()

	def turnSnakeRight(self) -> None:
		newSnake.moveRight()

	def moveSnakeForward(self) -> None:
		if 

	def _check_for_apple(self) -> bool:



		