import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    # Represent alien fleet
    def __init__(self, ai_game):
        # Alien starting position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load alien image and rect
        self.image = pygame.image.load('alien_invasion/images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start new aliens at top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store alien's horizontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        # Return True if alien is at edge of screen
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
          
    def update(self):
        # Move aliens right or left 
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
