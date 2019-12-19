#This is for snake game loop.

import pygame
from GameBoard import gameboard

moveSnakeForward = pygame.USEREVENT + 1
class SnakeGame(object):
	"""docstring for SnakeGame"""
	def __init__(self):
		super(SnakeGame, self).__init__()
		self._display_surface = (750,750)
		#something to help with gameplay
		self._game_play = gameboard()
		self._running = True

	def run(self):
		pygame.init()

		self._resize_surface(self._display_surface)

		clock = pygame.time.Clock()
		pygame.time.set_timer(moveSnakeForward, 1000)

		while self._running:
			clock.tick(30)
			#I don't remember this

			self._update_world()
			self._redraw()
			try:
			 	if self._game_play.check_game_over():
			 		self._running = False
			except:
				continue
		pygame.quit()

	def _update_world(self) -> None:
		"""Updtates the game based on game event changes"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self._quit_game()
			elif event.type == pygame.VIDEORESIZE:
				self._resize_surface(event.size)
			if event.type == moveSnakeForward:
			     self._game_play.move_snake_forward()
			if event.type == pygame.KEYDOWN:
				self._handle_keys_events(event)

	def _handle_keys_events(self, event) -> None:
		if event.key == pygame.K_LEFT:
			self._game_play.turn_snake_left()
		if event.key == pygame.K_RIGHT:
			self._game_play.turn_snake_right()
		if event.key == pygame.K_UP:
			self._game_play.turn_snake_up()
		if event.key == pygame.K_DOWN:
			self._game_play.turn_snake_down()
		if event.key == pygame.K_ESCAPE:
			pygame.quit()
			#Later on, implement a pause feature

	def _quit_game(self) -> None:
		"""Quits the game"""
		self._running = False

	def _resize_surface(self, size: (int, int)) -> None:
		"""Makes the game surface resizeable"""
		self._surface = pygame.display.set_mode(size, pygame.RESIZABLE)

	def _redraw(self):
		"""Draws the current surface of the game and the game board"""
		self._surface.fill(pygame.Color(48, 48, 48))
		self._display_game_board()
		pygame.display.flip()

	def _display_game_board(self) -> None:
		gameBoard = self._game_play.gameboard
		#pygame.draw.rect(self._surface, (247, 231, 54) , self._frac_to_pixel(self._coloumn_reference.coloumnSize(row, col)), 2)
		for row in range(15):
			for col in range(15):
				if gameBoard[row][col] == "A":
					pygame.draw.rect(self._surface, (242,78,78), self._frac_to_pixel(self._game_play.frac_proportions(row, col)))
				elif gameBoard[row][col] == "S":
					pygame.draw.rect(self._surface, (58,232,64), self._frac_to_pixel(self._game_play.frac_proportions(row, col)))


	def _frac_to_pixel(self, fracTuple: (float)) -> (int, int, int, int):
		"""Converts from fractional to pixel"""
		return (int(fracTuple[0] * self._surface.get_width()),int(fracTuple[1] * self._surface.get_height()),int(fracTuple[2] * self._surface.get_width()),int(fracTuple[3] * self._surface.get_height()))

if __name__ == '__main__':
	SnakeGame().run()