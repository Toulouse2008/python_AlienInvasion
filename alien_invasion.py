import sys
import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from alien import Alien 
import game_functions as gf

def run_game():
	#initialize game and create a screen object
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	alien = Alien(ai_settings,screen)
	ship = Ship(ai_settings,screen)
	bullets = Group()
	aliens = Group()

	gf.create_fleet(ai_settings,screen,ship,aliens)

	while True:

		#watch for keyboard and mouse events 
		gf.check_events(ai_settings,screen,ship,bullets)
		#update the ships positioning 
		ship.update()
		#update the bullets positioning 
		gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
		gf.update_aliens(ai_settings,ship,aliens)
		#update screen
		gf.update_screen(ai_settings,screen,ship,aliens,bullets)

run_game()

