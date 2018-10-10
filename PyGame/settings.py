class Settings():
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings."""

        # Screen settings
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 15
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 5
        self.bullet_height = 5
        self.bullet_color = 0, 0, 0
        self.bullets_allowed = 100

        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # Fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1