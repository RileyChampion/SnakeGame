#This is for snake game loop.

import pygame
import gameboard

class SnakeGame(object):
	"""docstring for SnakeGame"""
	def __init__(self, arg):
		super(SnakeGame, self).__init__()
		self._display_surface = (750,750)
		#something to help with gameplay
		#start game in init
		self._running = True

	def run(self):
		pygame.init()

		clock = pygame.time.Clock()
		#need a move forward timer

		while self._running:
			#clock.tick()
			#I don't remember this

			self._update_world()
			self._redraw()
			# try:
			# 	#check if it's game over
			# 	#stop the game
			# except:
		pygame.quit()

	def _update_world(self) -> None:
        """Updtates the game based on game event changes"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._quit_game()
            elif event.type == pygame.VIDEORESIZE:
                self._resize_surface(event.size)
            # if event.type == dropTimer:
            #     self._game_play.game_board_dropping()
            if event.type == pygame.KEYDOWN:
                self._handle_keys_events(event)

	def _handle_key_events(self, event) -> None:
		# if event.key == pygame.K_LEFT:

		# if event.key == pygame.K_RIGHT:

		if event.key == pygame.K_ESACPE:
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
    
    def _frac_to_pixel(self, fracTuple: (float)) -> (int, int, int, int):
        """Converts from fractional to pixel"""
        return (int(fracTuple[0] * self._surface.get_width()),int(fracTuple[1] * self._surface.get_height()),int(fracTuple[2] * self._surface.get_width()),int(fracTuple[3] * self._surface.get_height()))

