import pygame
from pygame.sprite import Sprite 

class Bullet(Sprite):

	def __init__(self,ai_settings,screen,ship):
		#create a bullet object from the ships current position

		super(Bullet,self).__init__()
		self.screen = screen

		#create a bullet at (0,0) and then set its position 
		self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		#store the bullets current position as a decimal
		self.y = float(self.rect.y)

		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bulletspeed


	def update(self):
		#move the bullet up the screen
		self.y-=self.speed_factor
		self.rect.y = self.y


	def draw_bullet(self):
		#draw the bullet to the screen 
		pygame.draw.rect(self.screen,self.color,self.rect)