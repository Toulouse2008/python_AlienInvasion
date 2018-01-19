import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''Alien object'''
    def __init__(self, screen_settings, screen):
        '''Initialize the alien and setup location'''
        super(Alien,self).__init__()
        self.screen = screen
        self.screen_settings = screen_settings
        #load bpm image
        self.image = pygame.image.load('./images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        '''Horizontal movement'''
        self.x += (self.screen_settings.alien_speed_factor * self.screen_settings.fleet_direction)
        self.rect.x = self.x


    def blitme(self):
        '''Draw the alien at its current location'''
        self.screen.blit(self.image, self.rect)
