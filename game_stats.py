import pygame
import json

class GameStats():
    """跟踪游戏统计信息"""

    def __init__(self,ai_settings):
        self.ai_settings = ai_settings
        try:
            with open('highscore.txt','r') as f_obj:
                high_score = f_obj.read()
                self.high_score = int(high_score)
        except FileNotFoundError:
            self.high_score = 0
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1