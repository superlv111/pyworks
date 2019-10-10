import pygame
import sys

from pygame.sprite import Sprite
from pygame.sprite import Group
from random import randint


class Star(Sprite):
    """创建星星"""

    def __init__(self,screen):
        super().__init__()
        self.screen = screen
        # 创建一个矩形
        self.rect = pygame.Rect(0,0,20,20)
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.color = (255,255,0)

    def draw_star(self):
        pygame.draw.rect(self.screen,self.color,self.rect)


def create_fleet(stars,screen):
    """创建星星们"""
    star = Star(screen)
    number_of_stars_x = 20
    number_of_rows = 15

    for row in range(number_of_rows):
        for number in range(number_of_stars_x):
            create_star(screen,stars,number,row)


def create_star(screen,stars,number,row):
    """生成并排列星星"""
    star = Star(screen)
    star_width = star.rect.width
    star_height = star.rect.height
    star.x = star_width + 3*star_width*number + randint(-20,20)
    star.y = star_height + 3*star_height*row + randint(-20,20)
    star.rect.x = star.x
    star.rect.y = star.y
    stars.add(star)


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Stars")
    stars = Group()

    create_fleet(stars,screen)

    while True:

        for star in stars.sprites():
            star.draw_star()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

run_game()
