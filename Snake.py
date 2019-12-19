#This is the module for the Snake Class

class snake(object):
	"""docstring for Snake"""
	def __init__(self) -> None:
		super(snake, self).__init__()
		self.head = [10,3]
		self.tail = [10,2]
		self._length = 2
		self.snake_array = [self.tail,self.head]
		self._direction = "east"
		self._prev_tail = []

	def moveForward(self) ->None:
		newHead = self.snake_array[self._length - 1][:]
		if self._direction == "north":
			newHead[0] -= 1
		elif self._direction == "south":
			newHead[0] += 1
		elif self._direction == "east":
			newHead[1] += 1
		elif self._direction == "west":
			newHead[1] -= 1
		self.snake_array.append(newHead)
		self._prev_tail = self.snake_array[0]
		self.snake_array = self.snake_array[1:]
		self.head = newHead
		self.tail = self.snake_array[0]

	#MoveUP
	def moveUp(self) -> None:
		if self._direction != "south" and self._direction != "north":
			self._direction = "north"

	#moveDown
	def moveDown(self) -> None:
		if self._direction != "north" and self._direction != "south":
			self._direction = "south"
		
	#moveLeft
	def moveLeft(self) -> None:
		if self._direction != "east" and self._direction != "west":
			self._direction = "west"

	#moveRight
	def moveRight(self) -> None:
		if self._direction != "west" and self._direction != "east":
			self._direction = "east"
	
	#eatApple
	def eatApple(self) -> None:
		self.snake_array = [self._prev_tail] + self.snake_array
		self._length += 1