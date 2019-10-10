import pygame
from ship import Ship
from pygame.sprite import Group

class ScoreBoard():
    """记分牌"""

    def __init__(self,ai_settings,screen,stats):
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.stats = stats

        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,50)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_left_ships()

    def prep_score(self):
        """绘制记分牌"""
        # 圆整得分
        rounded_score = int(round(self.stats.score,-1))
        score_str = "SCORE-"
        score_str += "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str,True,
            self.text_color,self.ai_settings.bg_color)

        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.right = self.screen_rect.right - 20
        self.score_image_rect.top = 20

    def prep_high_score(self):
        """绘制最高分"""
        # 圆整得分
        rounded_high_score = int(round(self.stats.high_score,-1))
        high_score_str = "HIGH SCORE-"
        high_score_str += "{:,}".format(rounded_high_score)
        self.high_score_image = self.font.render(high_score_str,True,
            self.text_color,self.ai_settings.bg_color)

        self.high_score_image_rect = self.high_score_image.get_rect()
        self.high_score_image_rect.centerx = self.screen_rect.centerx
        self.high_score_image_rect.top = 20

    def prep_level(self):
        """绘制等级显示"""
        level_str = "LEVEL-" + str(self.stats.level)
        self.level_image = self.font.render(level_str,True,
            self.text_color,self.ai_settings.bg_color)

        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.right = self.score_image_rect.right
        self.level_image_rect.top = self.score_image_rect.bottom + 10

    def prep_left_ships(self):
        self.left_ships = Group()
        for number in range((self.stats.ship_left-1)):
            ship_image = Ship(self.screen,self.ai_settings)
            ship_image.rect.left = 20 + number*(ship_image.rect.width + 10)
            ship_image.rect.top = 20
            self.left_ships.add(ship_image)

    def draw_scoreboard(self):
        self.screen.blit(self.score_image,self.score_image_rect)
        self.screen.blit(self.high_score_image,self.high_score_image_rect)
        self.screen.blit(self.level_image,self.level_image_rect)
        self.left_ships.draw(self.screen)
