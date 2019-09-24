class GameStats:
    # track statistics for alien invasion
    def __init__(self, ai_settings):
        # initialize statistics
        self.ai_settings = ai_settings
        self.reset_stats()
        # start alien invasion in an active state
        self.game_active = False

    def reset_stats(self):
        # initialize statistics that can change during the game
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0

# page 285, not working!


