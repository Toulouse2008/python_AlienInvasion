import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    '''A class to report scoring info'''
    def __init__(self, screen_settings, screen, stats):
        '''Initialize scorekeeping attributes'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.screen_settings = screen_settings
        self.stats = stats

        # set font for score info
        self.text_color = (50, 50, 50)
        self.font = pygame.font.SysFont(None, 50)
        # call prep_scrore
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_level(self):
        '''Render level info'''
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.screen_settings.bg_color)
        # level info position
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_score(self):
        '''Turn the score into a rendered image'''
        score_str = str(round(self.stats.score, -1))
        self.score_image = self.font.render(score_str, True, self.text_color, self.screen_settings.bg_color)

        # diaplay the score info at the top right
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 40

    def prep_high_score(self):
        high_score_str = str(round(self.stats.high_score, -1))
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.screen_settings.bg_color)

        # put the high score in the center
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        ''' Draw score info on the screen'''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # draw ships
        self.ships.draw(self.screen)

    def prep_ships(self):
        '''Show ships number on screen'''
        self.ships = Group()
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.screen_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
