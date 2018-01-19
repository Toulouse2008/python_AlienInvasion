class GameStats():
    def __init__(self, screen_settings):
        self.screen_settings = screen_settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        self.ship_left = self.screen_settings.ship_limit
