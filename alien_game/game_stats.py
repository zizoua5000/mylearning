class GameStats():
    """Track statistics for alien invasion"""

    def __init__(self, ai_settings):
        """initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Start Alien Invasion in an active state
        self.game_active = False
        # Score counter
        self.score = 0
        # hHigh score should never be reset
        self.high_score = 0



    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.ai_settings.ship_limit
