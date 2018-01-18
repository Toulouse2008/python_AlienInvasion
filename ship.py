import pygame
class Ship():
		def __init__(self,ai_settings,screen):
			#Iniialize the ship and sey its starting position 
			self.screen = screen
			# Load the ship image and get its rect
			self.image = pygame.image.load("./images/ship.bmp")
			self.rect = self.image.get_rect()
			self.screen_rect = screen.get_rect()
			# Start each new ship at the bottom center of the screen
			self.rect.centerx = self.screen_rect.centerx
			self.rect.bottom = self.screen_rect.bottom
			self.moving_right = False
			self.moving_left =False
			self.ai_settings = ai_settings 


		def update(self):
			if self.moving_right and self.rect.right<self.screen_rect.right:
				#setting left and right to true if we press down on left and right 
				self.rect.centerx+=self.ai_settings.speed
			elif self.moving_left and self.rect.left>0:
				self.rect.centerx-=self.ai_settings.speed



		def blitme(self):
			#Draw the ship at its current location
			self.screen.blit(self.image,self.rect)