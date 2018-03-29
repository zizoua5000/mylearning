import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """a class to represent a single alien in the fleet"""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = screen
        self.ai_settings  = ai_settings

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load("images/alien1_small.png")
        self.rect = self.image.get_rect()

        # Start each ne alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the aliens exact position
        self.x = float(self.rect.x)


    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)