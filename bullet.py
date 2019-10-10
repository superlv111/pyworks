import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """创建子弹的类"""

    def __init__(self,screen,ai_settings,ship):
        super().__init__()
        self.screen = screen
        # 在飞船处创建一个矩形
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,
            ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed = ai_settings.bullet_speed

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)