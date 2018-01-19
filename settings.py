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
