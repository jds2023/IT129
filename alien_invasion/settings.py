# This file contains the Settings class.
# This class only has an __init_() method, which initializes
# attributes controlling the game's appearance and the ship's speed.

class Settings:

  def __init__(self):
      #Initialize game's settings.
      self.screen_width = 1200
      self.screen_height = 800
      self.bg_color = (230, 230, 230)
      # Ship settings
      self.ship_speed = 1.5
      self.ship_limit = 3
      # Bullet settings
      self.bullet_speed = 1.5
      self.bullet_width = 3
      self.bullet_height = 15
      self.bullet_color = (60, 60, 60)
      self.bullets_allowed = 5
      # Alien settings
      self.alien_speed = 1.0
      self.fleet_drop_speed = 10
      # Fleet direction of 1 represents right; -1 left
      self.fleet_direction = 1 
