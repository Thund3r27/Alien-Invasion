class Settings:
    def __init__(self):
        #screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        #ship
        self.ship_limit = 3
        #bullet
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_limit = 3
        #alien
        self.fleet_drop_speed = 10
        #speed up rate
        self.speed_up_scale = 1.1
        self.score_scale = 1.5
        #speed changing as the game progresses
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        #self.fleet_direction value means right when 1 and left when -1
        self.fleet_direction = 1
        #scores
        self.alien_points = 50

    def increase_speed(self):
        """Speeding up the game"""
        self.ship_speed *= self.speed_up_scale
        self.bullet_speed *= self.speed_up_scale
        self.alien_speed *= self.speed_up_scale

        self.alien_points = int(self.alien_points * self.score_scale)