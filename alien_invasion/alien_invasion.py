import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    # Overall class to manage game assets and behavior.

    def __init__(self):

        #Initialize the game, and create game resources.
        pygame.init()
        self.settings = Settings()


        # Create the display window (aka surface) 1200 pixels wide by 800 pixels high
        # display variable set to self.screen so it is available to all methods in the class
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        # Set the background color of the display window
        #self.bg_color = (230, 230, 230)

    def run_game(self):
        # Start the main loop for the game.
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()
    
    # Detects relevant events, such as keypresses and releases
    # and processes these type of events using the _check_keydown_events
    # and _check_keyup_events

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            
    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events (self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    # Redraws the screen on each pass through the main loop
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

    # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()