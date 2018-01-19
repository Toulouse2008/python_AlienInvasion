import pygame

class Ship():
    def __init__(self, screen_settings, screen):
        '''Initialize the ship and set the starting position'''
        self.screen = screen
        self.screen_settings = screen_settings
        # load the ship image and set its rectangle location
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # store ship center
        self.center = float(self.rect.centerx)

        # movement flags
        self.moving_right = False
        self.moving_left = False

        # new ship appears from the bottom center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        '''Draw the ship at its current location'''
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx 

    def update(self):
        '''Update position based on movement flag'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.screen_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.screen_settings.ship_speed_factor
        self.rect.centerx = self.center
