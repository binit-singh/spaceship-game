import pygame
import time
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

# Local imports
from player import Player
from enemy import Enemy
from cloud import Cloud
from const import SCREEN_HEIGHT, SCREEN_WIDTH, COLOUR


class SpaceShipGame:
	def __init__(self):
		pygame.init()
		pygame.mixer.init()
		pygame.mixer.music.load('assets/sound/spaceship.mp3')
		pygame.mixer.music.play(loops=-1)
		self.running = True
		self.enemy_event = pygame.USEREVENT + 1
		self.cloud_event = pygame.USEREVENT + 2
		self.enemies = pygame.sprite.Group()
		self.clouds = pygame.sprite.Group()
		self.all_sprites = pygame.sprite.Group()

	def start(self):
		screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
		player = Player()
		self.trigger_cloud_event()
		self.trigger_enemy_event()
		self.all_sprites.add(player)
		# Game Loop
		while self.running:
			events = pygame.event.get()
			for event in events:
				if event.type == KEYDOWN and event.key == K_ESCAPE:
					self.running = False
				elif event.type == QUIT:
					self.running = False
				elif event.type == self.enemy_event:
					self.create_enemy()
				elif event.type == self.cloud_event:
					self.create_cloud()

			pressed_keys = pygame.key.get_pressed()
			player.update(pressed_keys)
			self.enemies.update()
			self.clouds.update()

			screen.fill(COLOUR['blue'])
			for entity in self.all_sprites:
				screen.blit(entity.surface, entity.rect)
			if pygame.sprite.spritecollideany(player, self.enemies):
				self.finish_collision(player)

			pygame.display.flip()

	def trigger_enemy_event(self):
		pygame.time.set_timer(self.enemy_event, 300)

	def create_enemy(self):
		new_enemy = Enemy()
		self.enemies.add(new_enemy)
		self.all_sprites.add(new_enemy)

	def create_cloud(self):
		new_cloud = Cloud()
		self.clouds.add(new_cloud)
		self.all_sprites.add(new_cloud)

	def trigger_cloud_event(self):
		pygame.time.set_timer(self.cloud_event, 1000)

	def finish_collision(self, player):
		player.kill()
		pygame.mixer.music.stop()
		collision_sound = pygame.mixer.Sound('assets/sound/collision.wav')
		collision_sound.play()
		time.sleep(1)
		self.running = False
