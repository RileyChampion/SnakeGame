#This is the module for the Snake Class

class snake(object):
	"""docstring for Snake"""
	def __init__(self):
		super(snake, self).__init__()
		self.head = [10,3]
		self.tail = [10,2]
		self._length = 2
		self.snake_array = [self.tail,self.head]
		self._direction = "east"

	def moveForward(self):
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
		self.snake_array = self.snake_array[1:]
		self.head = newHead
		self.tail = self.snake_array[0]
		
	#moveLeft
	def moveLeft(self):
		if self._direction == "north":
			self._direction = "west"
		elif self._direction == "south":
			self._direction = "east"
		elif self._direction == "east":
			self._direction = "north"
		elif self._direction == "west":
			self._direction = "south"

	#moveRight
	def moveRight(self):
		if self._direction == "north":
			self._direction = "east"
		elif self._direction == "south":
			self._direction = "west"
		elif self._direction == "east":
			self._direction = "south"
		elif self._direction == "west":
			self._direction = "north"
	
	#eatApple