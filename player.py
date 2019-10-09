import pygame
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT, RLEACCEL

# Local imports
from const import COLOUR, SCREEN_HEIGHT, SCREEN_WIDTH


class Player(pygame.sprite.Sprite):
	def __init__(self):
		super(Player, self).__init__()
		self.surface = pygame.image.load('assets/image/jet.png').convert()
		self.surface.set_colorkey(COLOUR['white'], RLEACCEL)
		self.rect = self.surface.get_rect()

	def update(self, pressed_keys):
		if pressed_keys[K_UP]:
			self.rect.move_ip(0, -5)
		if pressed_keys[K_DOWN]:
			self.rect.move_ip(0, 5)
		if pressed_keys[K_LEFT]:
			self.rect.move_ip(-5, 0)
		if pressed_keys[K_RIGHT]:
			self.rect.move_ip(5, 0)

		self.screen_limit()

	def screen_limit(self):

		if self.rect.left < 0:
			self.rect.left = 0

		if self.rect.right > SCREEN_WIDTH:
			self.rect.right = SCREEN_WIDTH

		if self.rect.top < 0:
			self.rect.top = 0

		if self.rect.bottom > SCREEN_HEIGHT:
			self.rect.bottom = SCREEN_HEIGHT

