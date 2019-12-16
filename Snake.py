#This is the module for the Snake Class

class Snake(object):
	"""docstring for Snake"""
	def __init__(self):
		super(Snake, self).__init__()
		self.head = [10,3]
		self.tail = [10,2]
		self._length_of_snake = 2
		self.snake_array = [self.tail,self.head]
		self._direction = "west"

	def moveForward(self):
		if direction == "north":
			#.. 
		elif direction == "south":
			#..
		elif direction == "east":
			#..
		elif direction == "west":
			#..
	#moveLeft
	def moveLeft(self):
		if direction == "north":
			self._direction = "west"
		elif direction == "south":
			self._direction = "east"
		elif direction == "east":
			self._direction = "north"
		elif direction == "west":
			self._direction = "south"
	#moveRight
	def moveRight(self):
		if direction == "north":
			self._direction = "east"
		elif direction == "south":
			self._direction = "west"
		elif direction == "east":
			self._direction = "south"
		elif direction == "west":
			self._direction = "north"
	#eatApple