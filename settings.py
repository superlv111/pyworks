class Settings():
    """储存各类设置"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (72,61,139)
        # 飞船设置
        # self.ship_speed = 1.5
        self.ship_limit = 3
        # 子弹设置
        # self.bullet_speed = 1
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (255,255,0)
        self.bullet_allowed = 5
        # 外星人设置
        # self.alien_speed = 1
        self.fleet_drop_speed = 10
        # self.fleet_direction = 1
        self.alien_points = 50
        # 初始化动态设置
        self.initialize_dynamic_settings()
        self.speedup_scale = 1.1
        self.alien_points_upscale = 1.5
        
    def initialize_dynamic_settings(self):
        self.alien_speed = 1
        self.bullet_speed = 2
        self.ship_speed = 1.5
        self.fleet_direction = 1

    def increase_game_pace(self):
        """随着进程提高游戏节奏"""
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.ship_speed *= self.speedup_scale
        self.alien_points *=self.alien_points_upscale
