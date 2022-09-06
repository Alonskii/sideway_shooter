class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 4

        # Bullet settings
        self.bullet_width = 4
        self.bullet_height = 8
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # Alien settings.
        # Alien_frequency controls the rate at which a new alien appears.
        # Higher values means more frequent aliens.
        self.alien_frequency = 0.005
        self.speedup_scale = 1.1

        self.Initialize_dynamic_settings()

    def Initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 2
        self.bullet_speed = 2.5
        self.alien_speed = 0.2

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
