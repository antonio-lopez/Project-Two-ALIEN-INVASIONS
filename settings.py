class Settings:
    # a class to store all settings for Alien invasion

    def __init__(self):
        # initialize the game's settings
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed_factor = 1.5

        # bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
