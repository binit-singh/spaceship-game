import pygame
import random
from pygame.locals import RLEACCEL

from const import COLOUR, SCREEN_HEIGHT, SCREEN_WIDTH


class Cloud(pygame.sprite.Sprite):
	def __init__(self):
		super(Cloud, self).__init__()
		self.surface = pygame.image.load('assets/image/cloud.png').convert()
		self.surface.set_colorkey(COLOUR['black'], RLEACCEL)
		self.rect = self.surface.get_rect(
			center=(
				random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
				random.randint(0, SCREEN_HEIGHT),
			)
		)

	def update(self):
		self.rect.move_ip(-5, 0)
		if self.rect.right < 0:
			self.kill()
