#Always start you game with this base.
import pygame, sys
from pygame.locals import *

pygame.init()

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()