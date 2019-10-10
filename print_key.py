import pygame
import sys


def check_events():
    """监视鼠标键盘事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print(event.key)
        elif event.type == pygame.KEYUP:
            print(event.key)

def update_screen(screen):
    """更新屏幕"""
    # 重绘背景色
    screen.fill((0,0,0))
    # 绘制最新的屏幕
    pygame.display.flip()


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption('Print Key')

    while True:
        check_events()
        update_screen(screen)


run_game()
