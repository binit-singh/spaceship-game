import random
import pygame
from pygame.locals import RLEACCEL

# Local imports
from const import COLOUR, SCREEN_WIDTH, SCREEN_HEIGHT


class Enemy(pygame.sprite.Sprite):
	def __init__(self):
		super(Enemy, self).__init__()
		self.surface = pygame.image.load('assets/image/missile.png').convert()
		self.surface.set_colorkey(COLOUR['white'], RLEACCEL)
		self.rect = self.surface.get_rect(
			center=(
				random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
				random.randint(0, SCREEN_HEIGHT)
			)
		)
		self.speed = random.randint(5, 20)

	def update(self):
		self.rect.move_ip(-self.speed, 0)
		if self.rect.right < 0:
			self.kill()