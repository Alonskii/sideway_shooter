from random import randint

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ss_game):
        """Initialize the alien and start it's starting positions."""
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('game/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien at random position, near the top right corner of the screen.
        self.rect.left = self.screen.get_rect().right

        # In order to get the position of the alien on the screen,
        # minus the height of the alien from the height of the screen.
        alien_up = self.settings.screen_height - self.rect.height
        self.rect.top = randint(0, alien_up)

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien to the left."""
        self.x -= self.settings.alien_speed
        self.rect.x = self.x
