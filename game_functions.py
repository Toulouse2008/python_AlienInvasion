import sys
import pygame
from alien import Alien 
from bullet import Bullet


def check_events(ai_settings,screen,ship,bullets):
	#keypresses and mouse presses
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			keydown_events(event,ai_settings,screen,ship,bullets)
		elif event.type == pygame.KEYUP:
			keyup_events(event,ship)
#update the screen
def update_screen(ai_settings,screen,ship,aliens,bullets):
	#update the screen through each pass through
	screen.fill(ai_settings.bg_color)
	ship.blitme()
	aliens.draw(screen)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	#Draw the most recent window to the screen 
	pygame.display.flip()


def keydown_events(event,ai_settings,screen,ship,bullets):
	if event.key == pygame.K_RIGHT:
	#move the ship to the right and left
		ship.moving_right = True
	elif event.key ==pygame.K_LEFT:
		ship.moving_left = True 
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings,screen,ship,bullets)
	elif event.key == pygame.K_q:
		sys.exit()


def keyup_events(event,ship):
	if event.key == pygame.K_RIGHT:
	#stop the ship from moving to the right and left
		ship.moving_right = False 
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def update_bullets(ai_settings,screen,ship,aliens,bullets):
	bullets.update()
	#get rid of the bullets that have disappeared
	for bullet in bullets.copy():
		if bullet.rect.bottom <=0:
			bullets.remove(bullet)

	collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)

	if len(aliens) == 0 and ai_settings.number_fleets > ai_settings.number_created:
		bullets.empty()
		create_fleet(ai_settings,screen,ship,aliens)
		ai_settings.number_created += 1
			
def fire_bullet(ai_settings,screen,ship,bullets):
	if len(bullets) < ai_settings.bullets_allowed:
			new_bullet = Bullet(ai_settings,screen,ship)
			bullets.add(new_bullet)
def get_na(ai_settings,alien_width):
	a_s = ai_settings.screen_width - (2*alien_width)
	n_o_a = int(a_s/(2*alien_width))
	return n_o_a

def create_alien(ai_settings,screen,aliens,a_n,row_number):
	alien = Alien(ai_settings,screen)
	alien_width = alien.rect.width
	alien.x = alien_width+(2*alien_width*a_n)
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)

def get_number_rows(ai_settings,ship_height,alien_height):
	a_s_y = (ai_settings.screen_height-(3*alien_height)-ship_height)
	n_r = int(a_s_y/(2*alien_height))
	return n_r

def check_fleet_edges(ai_settings,aliens):

	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings,aliens)
			break



def change_fleet_direction(ai_settings,aliens):
	for alien in aliens.sprites():
		alien.rect.y+=ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1

def create_fleet(ai_settings,screen,ship,aliens):
	alien = Alien(ai_settings,screen)
	number_aliens_x = get_na(ai_settings,alien.rect.width)
	number_row = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
	for row_number in range(number_row):
		for a_n in range(number_aliens_x):
			create_alien(ai_settings,screen,aliens,a_n,row_number)


def update_aliens(ai_settings,ship,aliens):
	check_fleet_edges(ai_settings,aliens)
	aliens.update()
	if pygame.sprite.spritecollideany(ship,aliens):
		print("Ship Hit!!")
		sys.exit()
		