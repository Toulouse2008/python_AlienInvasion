import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    ''' Class Bullet fired from the ship '''
    def __init__(self, screen_settings, screen, ship):
        '''constructor'''
        super(Bullet, self).__init__()
        self.screen = screen
        # create a rectangle as bullet and set up the location
        self.rect = pygame.Rect(0,0, screen_settings.bullet_width, screen_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)
        self.color = screen_settings.bullet_color
        self.speed_factor = screen_settings.bullet_speed_factor

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y


    def draw_bullet(self):
        '''Draw the bullet'''
        pygame.draw.rect(self.screen, self.color, self.rect)
