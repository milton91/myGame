import sys # untuk akses le sistem operasi secara universal

import pygame # library pygame untuk membangun game

class TheWitcher:

	#kerangka obejct untuk world dari game yang akan kita bangun
    def __init__(self):
    	pygame.init()

    	self.screen = pygame.display.set_mode([800,600])
    	self.title = pygame.display.set_caption("The Witcher")

    def run_game(self):

    	while True: #infinite loop

    		#monitoring kejadian / event
    		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
    				sys.exit()

    		#rendering display every frame
    		pygame.display.flip()

my_game = TheWitcher()
my_game.run_game()

