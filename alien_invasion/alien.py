import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    # Represent alien fleet
    def __init__(self, ai_game):
        # Alien starting position
        super().__init__()
        self.screen = ai_game.screen

        # Load alien image and rect
        self.image = pygame.image.load('alien_invasion/images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start new aliens at top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store alien's horizontal position
        self.x = float(self.rect.x)