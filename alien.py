import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """外星人的类"""

    def __init__(self,ai_settings,screen):
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        self.image = pygame.image.load('image/alien.png')
        self.image = pygame.transform.scale(self.image,(80,80))
        self.rect = self.image.get_rect()

        # 初始位置放在左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        self.x += (self.ai_settings.alien_speed * 
            self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edge(self):
        """检查外星人是否在屏幕边缘"""
        screen_rect = self.screen.get_rect()
        if self.rect.left < screen_rect.left:
            return True
        elif self.rect.right > screen_rect.right:
            return True
