import json

class GameStats:
    def __init__(self, ai_game):
        #game on or game over flag
        self.game_active = False
        self.settings = ai_game.settings
        filename = 'best_score.json'
        with open(filename, 'r') as f:
            self.high_score = json.load(f)
        self.reset_stats()
        
    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        filename = 'best_score.json'
        with open(filename, 'w') as f:
            json.dump(self.high_score, f)
            