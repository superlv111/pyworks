import pygame

class Button():
    """创建按钮类"""

    def __init__(self,screen,msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width,self.height = 200,50
        self.button_color = (0,255,255)
        self.text_color = (255,255,255)
        # 设置字体
        self.font = pygame.font.SysFont(None,48)
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center
        # 渲染字体
        self.msg_image = self.font.render(msg,True,self.text_color,
            self.button_color)
        self.msg_image_rect =self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        "绘制按钮"
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)