import sys
import pygame
from pygame.sprite import Group
from game_stats import GameStats

from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien

def run_game():
    # Initialize game and create a screen
    pygame.init()
    screen_settings = Settings()
    screen = pygame.display.set_mode((screen_settings.screen_width, screen_settings.screen_height))
    pygame.display.set_caption("Alert: Alien Ivasion")

    # game statistics
    stats = GameStats(screen_settings)
    # background color.
    bg_color = (230, 230, 230)
    # create a ship, a group of bullets/alien
    ship = Ship(screen_settings, screen)
    bullets = Group()
    aliens = Group()
    # fleet of aliens
    gf.create_fleet(screen_settings, screen, ship, aliens)

    #start the main loop for the gun_game
    while True:
        gf.check_events(screen_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(screen_settings, screen, ship, aliens, bullets)
            gf.update_aliens(screen_settings, stats, screen, ship, aliens, bullets)
        # destroy bullet once dispeared from the screen
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        gf.update_screen(screen_settings, screen, ship, aliens, bullets)

# call the rung_game() function
run_game()
