class GameStats:
    # Track statistics for Alien Invasion
    def __init__(self, ai_game):
        # Initialize stats
        self.settings = ai_game.settings
        self.reset_stats()
        # Start Alien Invasion in active state
        self.game_active = True

    def reset_stats(self):
        # Initialize changing stats
        self.ships_left = self.settings.ship_limit