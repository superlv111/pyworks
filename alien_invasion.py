import pygame
import sys
import json
import game_functions as gf

from pygame.sprite import Group

from settings import Settings

from ship import Ship
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard


def run_game():
    # 初始化游戏并创建屏幕

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
        ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建按钮
    play_button = Button(screen,"Play")

    # 创建飞船
    ship = Ship(screen,ai_settings)

    # 创建子弹组
    bullets = Group()

    # 创建外星人
    aliens = Group()
    gf.create_fleet(aliens,screen,ai_settings,ship)

    # 创建游戏统计信息库
    stats = GameStats(ai_settings)

    # 创建记分牌
    scoreboard = ScoreBoard(ai_settings,screen,stats)

    # 游戏主循环
    while True:
        gf.check_events(play_button,stats,ai_settings,aliens,
            bullets,ship,screen,scoreboard)

        if stats.game_active:
            ship.update()
            gf.update_bullets(bullets,aliens,ai_settings,ship,screen,
                stats,scoreboard)
            gf.update_aliens(ai_settings,aliens,ship,bullets,screen,stats,
                scoreboard)
            
        gf.update_screen(ship,screen,ai_settings,bullets,aliens,
            stats,play_button,scoreboard)
   

run_game()
