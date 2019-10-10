import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """创建一艘飞船"""

    def __init__(self,screen,ai_settings):
        """初始化飞船及其位置"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载飞船图像并抽象其外形
        self.image = pygame.image.load('image/ship.png')
        self.image = pygame.transform.scale(self.image,(80,56))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将飞船置于底边中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # 飞船位置记号（为了解决rect不能处理小数的问题）
        self.centerx = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)
        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)

    def update(self):
        """更新飞船位置"""
        if self.moving_right and self.centerx < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed
        # 针对同时按下左右键的情况使用的两个if增加控制准确度
        if self.moving_left and self.centerx > self.screen_rect.left:
            self.centerx -= self.ai_settings.ship_speed
        if self.moving_down and self.bottom < self.screen_rect.bottom:
            self.bottom += self.ai_settings.ship_speed
        if self.moving_up and self.bottom > self.rect.height:
            self.bottom -= self.ai_settings.ship_speed
        self.rect.centerx = self.centerx
        self.rect.bottom = self.bottom

    def center_ship(self):
        """飞船位置重置"""
        self.centerx = self.screen_rect.centerx
        self.bottom = self.screen_rect.bottom
        self.rect.centerx = self.centerx
        self.rect.bottom = self.bottom
