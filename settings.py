class Settings():
    ''' Class to store setting parameters'''
    def __init__(self):
        '''Initialize the game settings'''
        # screen parameters: width, height, and color
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # ship speed factor
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # bullet settings
        self.bullets_allowed = 3
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color =60, 60, 60

        # alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        # game speeds up
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()
        # score speedup factor
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        '''Initialize settings'''
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1.1
        # 1==>right -1==>left
        self.fleet_direction = 1
        # score
        self.alien_points = 50

    def increase_speed(self):
        '''Increase the speed and point values'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
