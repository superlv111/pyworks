import pygame
import sys

def check_keydown_events(event,rocket):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = True
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = True
    elif event.key == pygame.K_UP:
        rocket.moving_up = True
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = True

def check_keyup_events(event,rocket):
    """响应松开按键"""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = False
    elif event.key == pygame.K_UP:
        rocket.moving_up = False
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = False

def check_events(rocket):
    """监视鼠标键盘事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,rocket)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,rocket)

def update_screen(rocket,screen):
    """更新屏幕"""
    # 重绘背景色
    screen.fill((0,0,0))
    rocket.blitme()
    # 绘制最新的屏幕
    pygame.display.flip()

class Rocket():
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load('image/rocket.png')
        self.image = pygame.transform.smoothscale(self.image,(150,180))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_left and self.rect.centerx > self.screen_rect.left:
            self.rect.centerx -= 1
        if self.moving_right and self.rect.centerx < self.screen_rect.right:
            self.rect.centerx += 1
        if self.moving_up and self.rect.centery > self.screen_rect.top:
            self.rect.centery -= 1
        if self.moving_down and self.rect.centery < self.screen_rect.bottom:
            self.rect.centery += 1

    def blitme(self):
        self.screen.blit(self.image,self.rect)

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption('Rocket')
    rocket = Rocket(screen)

    while True:
        check_events(rocket)
        rocket.update()
        update_screen(rocket,screen)


run_game()
